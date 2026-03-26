"use client";
import React, { useEffect, useRef, useState } from 'react';
import maplibregl from 'maplibre-gl';
import axios from 'axios';
import Link from 'next/link';
import 'maplibre-gl/dist/maplibre-gl.css';
import { MapPin, ShieldAlert, Wallet, Building2, Sparkles, Search, X, ChevronDown, BarChart3, Users, User, Trophy } from 'lucide-react'; 
import AnalysisModal from './AnalysisModal'; 
import WardComparisonChart from './WardComparisonChart';
import { getPartyLogoUrl } from './partyLogos';

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:8000';

interface MapInterfaceProps {
    isPreview?: boolean;
}

export default function MapInterface({ isPreview = false }: MapInterfaceProps) {
  const mapContainer = useRef<HTMLDivElement>(null);
  const map = useRef<maplibregl.Map | null>(null);
  
  // Data States
  const [info, setInfo] = useState<any>(null);
  const [geoData, setGeoData] = useState<any>(null); 
  const [states, setStates] = useState<string[]>([]);
  const [selectedState, setSelectedState] = useState("MAHARASHTRA");

  // Search States
  const [searchQuery, setSearchQuery] = useState("");
  const [suggestions, setSuggestions] = useState<any[]>([]);
  const [candidateSuggestions, setCandidateSuggestions] = useState<any[]>([]);
  const [isSearchFocused, setIsSearchFocused] = useState(false);
  const [searchMode, setSearchMode] = useState<'ward' | 'candidate'>('ward');
  const candidateSearchTimer = useRef<NodeJS.Timeout | null>(null);

  // AI States
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [aiData, setAiData] = useState<any>(null);
  const [isAiLoading, setIsAiLoading] = useState(false);

  // Ward Comparison States
  const [wardStats, setWardStats] = useState<any>(null);
  const [showComparison, setShowComparison] = useState(false);
  const [isWardStatsLoading, setIsWardStatsLoading] = useState(false);

  // Cinematic Coordinates (Mumbai Center)
  const PREVIEW_COORDS = { lng: 72.8777, lat: 19.0760 }; 

  // --- 1. FETCH STATES ON LOAD (Only needed for dropdown) ---
  useEffect(() => {
    if (!isPreview) {
        const fetchStates = async () => {
            try {
                const res = await axios.get(`${API_BASE}/api/states`);
                setStates(res.data);
            } catch (e) { console.error("Failed to load states"); }
        };
        fetchStates();
    }
  }, [isPreview]);

  // --- 2. LOAD MAP SHAPES ---
  const loadShapes = async (stateName: string) => {
      try {
          const response = await axios.get(`${API_BASE}/api/shapes?state=${stateName}`);
          if (response.data && response.data.features) {
              setGeoData(response.data); 
              
              const source = map.current?.getSource('constituencies') as maplibregl.GeoJSONSource;
              if (source) {
                  source.setData(response.data);
              } else {
                  // Initial Load
                  map.current?.addSource('constituencies', { type: 'geojson', data: response.data });
                  
                  // Fill Layer
                  map.current?.addLayer({
                      'id': 'constituency-fills', 'type': 'fill', 'source': 'constituencies',
                      'paint': { 'fill-color': '#3b82f6', 'fill-opacity': isPreview ? 0.15 : 0.1 } // Slightly darker in preview for contrast
                  });
                  
                  // Border Layer
                  map.current?.addLayer({
                      'id': 'constituency-borders', 'type': 'line', 'source': 'constituencies',
                      'paint': { 'line-color': '#2563eb', 'line-width': isPreview ? 2 : 1.5 }
                  });

                  // Labels (Hide in preview to keep it clean, show in App)
                  if (!isPreview) {
                      map.current?.addLayer({
                          'id': 'constituency-labels', 'type': 'symbol', 'source': 'constituencies', 'minzoom': 9, 
                          'layout': {
                              'text-field': ['format', ['get', 'name'], { 'font-scale': 1.0 }, '\n', {}, '(', {}, ['get', 'ac_no'], {}, ')', {}],
                              'text-font': ['Open Sans Bold', 'Arial Unicode MS Bold'], 'text-size': 11, 'text-transform': 'uppercase',
                              'text-anchor': 'center', 'text-max-width': 8 
                          },
                          'paint': { 'text-color': '#1e3a8a', 'text-halo-color': '#ffffff', 'text-halo-width': 2 }
                      });
                  }

                  // Hover Effect
                  map.current?.addLayer({
                      'id': 'constituency-hover', 'type': 'line', 'source': 'constituencies',
                      'paint': { 'line-color': '#f97316', 'line-width': 3 }, 'filter': ['==', 'name', ''] 
                  });
              }

              // --- SMART ZOOM LOGIC ---
              // Only Auto-Zoom in FULL APP MODE. 
              // In Preview, we want the cinematic manual angle.
              if (!isPreview && response.data.features.length > 0) {
                  const bounds = new maplibregl.LngLatBounds();
                  response.data.features.forEach((feature: any) => {
                      if (feature.geometry.type === "Polygon") {
                          feature.geometry.coordinates[0].forEach((coord: any) => bounds.extend(coord));
                      } else if (feature.geometry.type === "MultiPolygon") {
                          feature.geometry.coordinates.forEach((poly: any) => {
                              poly[0].forEach((coord: any) => bounds.extend(coord));
                          });
                      }
                  });
                  map.current?.fitBounds(bounds, { padding: 50, duration: 2000 });
              }
          }
      } catch (e) { console.error("Failed to load map shapes:", e); }
  };

  const handleStateChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
      const newState = e.target.value;
      setSelectedState(newState);
      loadShapes(newState);
      setInfo(null);
  };

  // --- SEARCH LOGIC ---
  const handleSearch = (e: React.ChangeEvent<HTMLInputElement>) => {
      const query = e.target.value;
      setSearchQuery(query);

      if (searchMode === 'ward') {
          // Ward mode: search GeoJSON features locally
          if (query.length > 1 && geoData) {
              const matches = geoData.features.filter((f: any) => {
                  const name = f.properties.name;
                  return name && typeof name === 'string' && name.toLowerCase().includes(query.toLowerCase());
              });
              setSuggestions(matches.slice(0, 5));
          } else {
              setSuggestions([]);
          }
          setCandidateSuggestions([]);
      } else {
          // Candidate mode: debounced API call
          setSuggestions([]);
          if (candidateSearchTimer.current) clearTimeout(candidateSearchTimer.current);
          if (query.length > 1) {
              candidateSearchTimer.current = setTimeout(async () => {
                  try {
                      const res = await axios.get(`${API_BASE}/api/search-candidates?q=${encodeURIComponent(query)}`);
                      setCandidateSuggestions(res.data || []);
                  } catch { setCandidateSuggestions([]); }
              }, 300);
          } else {
              setCandidateSuggestions([]);
          }
      }
  };

  const handleSearchModeToggle = (mode: 'ward' | 'candidate') => {
      setSearchMode(mode);
      setSearchQuery('');
      setSuggestions([]);
      setCandidateSuggestions([]);
  };

  const selectResult = (feature: any) => {
      setSearchQuery(feature.properties.name);
      setSuggestions([]);
      setIsSearchFocused(false);

      const coordinates = feature.geometry.coordinates[0];
      const bounds = new maplibregl.LngLatBounds();
      
      if (feature.geometry.type === "Polygon") {
         coordinates.forEach((coord: any) => bounds.extend(coord));
      } else if (feature.geometry.type === "MultiPolygon") {
         feature.geometry.coordinates.forEach((poly: any) => {
             poly[0].forEach((coord: any) => bounds.extend(coord));
         });
      }

      const center = bounds.getCenter();
      map.current?.flyTo({ center: center, zoom: 14, pitch: 50, bearing: 10, speed: 1.5 });
      setTimeout(() => fetchVicinityData(center.lat, center.lng), 1000);
  };

  const selectCandidateResult = (candidate: any) => {
      setSearchQuery(candidate.name);
      setCandidateSuggestions([]);
      setIsSearchFocused(false);

      // Find the ward feature in geoData to fly to it
      if (geoData) {
          const wardFeature = geoData.features.find((f: any) => {
              const name = f.properties.name;
              return name && typeof name === 'string' &&
                  (name.toLowerCase() === candidate.ward.toLowerCase() ||
                   name.toLowerCase().includes(candidate.ward.toLowerCase()) ||
                   candidate.ward.toLowerCase().includes(name.toLowerCase()));
          });

          if (wardFeature) {
              selectResult(wardFeature);
              return;
          }
      }

      // Fallback: just fetch ward stats directly
      fetchWardStats(candidate.ward);
  };

  const fetchWardStats = async (wardName: string) => {
      setIsWardStatsLoading(true);
      try {
          const res = await axios.get(`${API_BASE}/api/ward-stats?ward=${encodeURIComponent(wardName)}`);
          if (res.data && res.data.available !== false) {
              setWardStats(res.data);
          } else {
              setWardStats(null);
          }
      } catch (e) {
          // Silently handle – ward data is simply unavailable
          setWardStats(null);
      } finally {
          setIsWardStatsLoading(false);
      }
  };

  const fetchVicinityData = async (lat: number, lng: number) => {
      setInfo({ loading: true });
      setShowComparison(false);
      try {
          const response = await axios.post(`${API_BASE}/api/vicinity`, { latitude: lat, longitude: lng });
          setInfo(response.data);
          // Also kick off ward stats fetch for the comparison chart
          if (response.data?.mla_constituency && response.data.mla_constituency !== 'Not Found') {
              fetchWardStats(response.data.mla_constituency);
          }
      } catch (error) { setInfo({ error: "Connection failed." }); }
  };

  const handleAnalyze = async () => {
      if (!info) return;
      setIsModalOpen(true);
      setIsAiLoading(true);
      try {
          const response = await axios.post(`${API_BASE}/api/analyze`, {
              name: info.mla_candidate,
              party: info.mla_party,
              cases: info.mla_cases,
              assets: info.mla_assets
          });
          setAiData(response.data);
      } catch (e) { console.error(e); } finally { setIsAiLoading(false); }
  };

  useEffect(() => {
    if (map.current || !mapContainer.current) return;

    map.current = new maplibregl.Map({
      container: mapContainer.current,
      style: 'https://tiles.openfreemap.org/styles/liberty', 
      center: [PREVIEW_COORDS.lng, PREVIEW_COORDS.lat], // Always start at Mumbai
      zoom: isPreview ? 11.5 : 10, // Slightly closer in preview
      pitch: isPreview ? 65 : 45, // More dramatic angle in preview
      bearing: isPreview ? -15 : 0,
      interactive: !isPreview,
      attributionControl: false,
    });

    map.current.on('load', async () => {
        // Load Maharashtra by default for both
        loadShapes("MAHARASHTRA");
    });

    if (!isPreview) {
        map.current.addControl(new maplibregl.NavigationControl(), 'top-right');
        
        map.current.on('click', async (e) => {
            const { lng, lat } = e.lngLat;
            map.current?.flyTo({ center: [lng, lat], zoom: 14, pitch: 50, speed: 1.5 });
            setTimeout(() => fetchVicinityData(lat, lng), 300);
        });
        
        map.current.on('mousemove', 'constituency-fills', (e) => {
            if (e.features && e.features.length > 0) {
                const name = e.features[0].properties.name;
                if (name) { 
                    map.current?.setFilter('constituency-hover', ['==', 'name', name]);
                    map.current!.getCanvas().style.cursor = 'pointer';
                }
            }
        });
        map.current.on('mouseleave', 'constituency-fills', () => {
            map.current?.setFilter('constituency-hover', ['==', 'name', '']);
            map.current!.getCanvas().style.cursor = '';
        });
    }

    if (isPreview) {
        let frame = 0;
        const rotateCamera = () => {
            if (!map.current) return;
            const bearing = map.current.getBearing();
            map.current.setBearing(bearing + 0.05); 
            frame = requestAnimationFrame(rotateCamera);
        };
        rotateCamera();
        return () => cancelAnimationFrame(frame);
    }
  }, [isPreview]);

  const jumpToDemo = () => {
      map.current?.flyTo({ center: [73.296, 19.296], zoom: 13.5, pitch: 60, speed: 1.2 });
  };

  const getPartyColor = (party: string) => {
      if (!party) return "bg-gray-100 border-gray-300";
      if (party.includes("Shiv Sena") || party.includes("BJP")) return "bg-orange-50 border-orange-200 text-orange-900";
      if (party.includes("Congress") || party.includes("NCP")) return "bg-blue-50 border-blue-200 text-blue-900";
      return "bg-green-50 border-green-200 text-green-900"; 
  };

  return (
    <div style={{ width: '100%', height: '100%', position: 'relative', overflow: 'hidden' }}>
      <div ref={mapContainer} style={{ position: 'absolute', top: 0, bottom: 0, left: 0, right: 0, zIndex: 0 }} />
      
      {/* UI OVERLAY - ONLY RENDER IF NOT IN PREVIEW MODE */}
      {!isPreview && (
          <>
            <div className="absolute top-0 left-0 w-full bg-gradient-to-b from-white/90 to-transparent p-4 z-10 pointer-events-none">
                <div className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center pointer-events-auto gap-4">
                    
                    <div className="flex items-center gap-4 shrink-0">
                        <Link href="/" className="hover:opacity-80 transition-opacity">
                            <h1 className="text-2xl font-black tracking-tight text-blue-900 cursor-pointer shadow-sm">
                                Candidate<span className="text-blue-500">Validate</span>
                            </h1>
                        </Link>
                        
                        {/* STATE DROPDOWN (Hidden in Preview) */}
                        <div className="relative">
                            <select 
                                value={selectedState} 
                                onChange={handleStateChange}
                                className="appearance-none bg-white/90 backdrop-blur border border-gray-200 text-slate-700 font-bold text-xs py-2 pl-4 pr-8 rounded-full shadow-sm hover:bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 cursor-pointer uppercase tracking-wide"
                            >
                                {states.map(st => (
                                    <option key={st} value={st}>{st}</option>
                                ))}
                            </select>
                            <ChevronDown className="absolute right-3 top-2.5 text-slate-400 pointer-events-none" size={14} />
                        </div>
                    </div>

                    {/* SEARCH BAR WITH INLINE MODE TOGGLE */}
                    <div className="relative w-full max-w-lg mx-4">
                        <div className="flex items-center bg-white/95 backdrop-blur-sm rounded-full border border-gray-300 shadow-lg focus-within:ring-2 focus-within:ring-blue-500 focus-within:border-blue-500 overflow-hidden">
                            {/* Inline Toggle Pills */}
                            <div className="flex items-center shrink-0 bg-gray-100/80 rounded-full m-1 p-0.5">
                                <button
                                    onClick={() => handleSearchModeToggle('ward')}
                                    className={`flex items-center gap-1 px-3 py-1.5 rounded-full text-[11px] font-bold uppercase tracking-wide transition-all duration-200 ${
                                        searchMode === 'ward'
                                            ? 'bg-white text-blue-700 shadow-sm'
                                            : 'text-gray-400 hover:text-gray-600'
                                    }`}
                                >
                                    <Building2 size={11} /> Ward
                                </button>
                                <button
                                    onClick={() => handleSearchModeToggle('candidate')}
                                    className={`flex items-center gap-1 px-3 py-1.5 rounded-full text-[11px] font-bold uppercase tracking-wide transition-all duration-200 ${
                                        searchMode === 'candidate'
                                            ? 'bg-white text-blue-700 shadow-sm'
                                            : 'text-gray-400 hover:text-gray-600'
                                    }`}
                                >
                                    <User size={11} /> Candidate
                                </button>
                            </div>

                            {/* Search Input */}
                            <input 
                                type="text" 
                                placeholder={searchMode === 'ward' ? `Search in ${selectedState}...` : 'Search by name...'}
                                className="flex-1 min-w-0 py-2.5 pr-9 pl-2 outline-none text-sm font-medium bg-transparent"
                                value={searchQuery}
                                onChange={handleSearch}
                                onFocus={() => setIsSearchFocused(true)}
                                onBlur={() => setTimeout(() => setIsSearchFocused(false), 200)} 
                            />
                            {searchQuery ? (
                                <button onClick={() => { setSearchQuery(''); setSuggestions([]); setCandidateSuggestions([]); }} className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600">
                                    <X size={16} />
                                </button>
                            ) : (
                                <Search className="absolute right-3.5 top-1/2 -translate-y-1/2 text-gray-400" size={16} />
                            )}
                        </div>

                        {/* WARD DROPDOWN RESULTS */}
                        {isSearchFocused && searchMode === 'ward' && suggestions.length > 0 && (
                            <div className="absolute top-full left-0 w-full mt-2 bg-white rounded-xl shadow-2xl border border-gray-100 overflow-hidden animate-in slide-in-from-top-2 duration-200 z-50">
                                {suggestions.map((feature, i) => (
                                    <button 
                                        key={i}
                                        onClick={() => selectResult(feature)}
                                        className="w-full text-left px-4 py-3 hover:bg-blue-50 border-b border-gray-50 last:border-0 flex items-center justify-between group transition-colors"
                                    >
                                        <span className="font-semibold text-slate-700 group-hover:text-blue-700">{feature.properties.name}</span>
                                        <span className="text-xs text-slate-400 bg-slate-100 px-2 py-0.5 rounded group-hover:bg-blue-100 group-hover:text-blue-600">
                                            #{feature.properties.ac_no}
                                        </span>
                                    </button>
                                ))}
                            </div>
                        )}

                        {/* CANDIDATE DROPDOWN RESULTS */}
                        {isSearchFocused && searchMode === 'candidate' && candidateSuggestions.length > 0 && (
                            <div className="absolute top-full left-0 w-full mt-2 bg-white rounded-xl shadow-2xl border border-gray-100 overflow-hidden animate-in slide-in-from-top-2 duration-200 z-50">
                                {candidateSuggestions.map((c: any, i: number) => (
                                    <button
                                        key={i}
                                        onClick={() => selectCandidateResult(c)}
                                        className="w-full text-left px-4 py-3 hover:bg-blue-50 border-b border-gray-50 last:border-0 flex items-start gap-3 group transition-colors"
                                    >
                                        <div className="w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center shrink-0 mt-0.5">
                                            <img src={getPartyLogoUrl(c.party)} alt={c.party} className="w-5 h-5 object-contain" />
                                        </div>
                                        <div className="min-w-0 flex-1">
                                            <div className="flex items-center gap-2">
                                                <span className="font-semibold text-slate-700 group-hover:text-blue-700 truncate">{c.name}</span>
                                                {c.is_winner && (
                                                    <span className="flex items-center gap-0.5 text-[10px] font-bold bg-amber-100 text-amber-700 px-1.5 py-0.5 rounded-full shrink-0">
                                                        <Trophy size={9} /> Winner
                                                    </span>
                                                )}
                                            </div>
                                            <div className="flex items-center gap-2 mt-0.5">
                                                <span className="text-[11px] text-slate-400 font-medium">{c.party}</span>
                                                <span className="text-[10px] text-slate-400">•</span>
                                                <span className="text-[11px] text-blue-500 font-semibold">{c.ward}</span>
                                            </div>
                                        </div>
                                    </button>
                                ))}
                            </div>
                        )}
                    </div>

                    <button onClick={jumpToDemo} className="bg-gray-900 text-white text-xs font-bold px-4 py-2 rounded-full shadow-lg hover:bg-gray-800 transition-all flex items-center gap-2 shrink-0">
                        <MapPin size={14} /> LOCATE ME
                    </button>
                </div>
            </div>

            <AnalysisModal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} data={aiData} isLoading={isAiLoading} />

            {/* CANDIDATE INFO CARD */}
            {info && (
                <div className="absolute bottom-8 left-4 md:left-8 z-20 w-full max-w-sm animate-in slide-in-from-bottom-10 fade-in duration-500">
                    <div className="bg-white rounded-2xl shadow-2xl overflow-hidden border border-gray-100">
                        {info.loading ? (
                            <div className="p-8 text-center">
                                <div className="w-8 h-8 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mx-auto mb-3"></div>
                                <p className="text-gray-500 font-medium text-sm">Analyzing Constituency Data...</p>
                            </div>
                        ) : info.error ? (
                            <div className="p-6 text-center text-red-500">
                                <ShieldAlert className="mx-auto mb-2" />
                                <p>{info.error}</p>
                            </div>
                        ) : (
                            <div>
                                <div className="bg-gray-50 px-6 py-3 border-b border-gray-100 flex justify-between items-center">
                                    <div className="flex items-center gap-2 text-gray-500">
                                        <Building2 size={16} />
                                        <span className="text-xs font-bold uppercase tracking-wider">{info.mla_constituency}</span>
                                    </div>
                                    <span className="text-xs bg-gray-200 text-gray-600 px-2 py-1 rounded font-bold">MLA</span>
                                </div>

                                <div className={`p-6 border-l-4 ${getPartyColor(info.mla_party)}`}>
                                    <div className="flex items-start gap-4">
                                        <div className="w-12 h-12 rounded-full overflow-hidden border-2 border-gray-100 shadow-sm shrink-0 bg-white flex items-center justify-center">
                                            <img src={getPartyLogoUrl(info.mla_party)} alt={info.mla_party} className="w-9 h-9 object-contain" />
                                        </div>
                                        <div>
                                            <h2 className="text-xl font-bold text-gray-900 leading-tight">{info.mla_candidate}</h2>
                                            <p className="text-sm font-medium opacity-80 mt-1">{info.mla_party}</p>
                                        </div>
                                    </div>

                                    <div className="grid grid-cols-2 gap-4 mt-6">
                                        <div className="bg-white/60 p-3 rounded-lg border border-gray-200/50">
                                            <p className="text-[10px] text-gray-500 uppercase font-bold mb-1">Criminal Cases</p>
                                            <div className="flex items-center gap-2 text-red-600 font-black text-lg">
                                                <ShieldAlert size={18} />
                                                {info.mla_cases}
                                            </div>
                                        </div>
                                        <div className="bg-white/60 p-3 rounded-lg border border-gray-200/50">
                                            <p className="text-[10px] text-gray-500 uppercase font-bold mb-1">Declared Assets</p>
                                            <div className="flex items-center gap-2 text-green-600 font-black text-lg">
                                                <Wallet size={18} />
                                                {info.mla_assets}
                                            </div>
                                        </div>
                                    </div>
                                    
                                    {/* ASPIRING CANDIDATES LIST */}
                                    {wardStats && wardStats.candidates && wardStats.candidates.length > 0 && (
                                        <div className="mt-5">
                                            <p className="text-[10px] text-gray-500 uppercase font-bold tracking-wider mb-2 flex items-center gap-1.5">
                                                <Users size={12} /> Aspiring Candidates ({wardStats.candidates.length})
                                            </p>
                                            <div className="max-h-[180px] overflow-y-auto space-y-1.5 pr-1 scrollbar-thin">
                                                {wardStats.candidates.map((c: any, i: number) => (
                                                    <div key={i} className="flex items-center justify-between bg-white/80 border border-gray-100 rounded-lg px-3 py-2 hover:bg-gray-50 transition-colors">
                                                        <div className="w-7 h-7 rounded-full overflow-hidden border border-gray-100 shadow-sm shrink-0 bg-white flex items-center justify-center mr-2">
                                                            <img src={getPartyLogoUrl(c.party)} alt={c.party} className="w-5 h-5 object-contain" />
                                                        </div>
                                                        <div className="min-w-0 flex-1">
                                                            <p className="text-xs font-semibold text-slate-800 truncate">{c.name}</p>
                                                            <p className="text-[10px] text-slate-400 font-medium">{c.party}</p>
                                                        </div>
                                                        <div className="flex items-center gap-2 shrink-0 ml-2">
                                                            <span className={`text-[10px] font-bold px-1.5 py-0.5 rounded ${
                                                                c.cases === 0 ? 'bg-green-50 text-green-600' :
                                                                c.cases <= 2 ? 'bg-amber-50 text-amber-600' :
                                                                'bg-red-50 text-red-600'
                                                            }`}>
                                                                {c.cases} case{c.cases !== 1 ? 's' : ''}
                                                            </span>
                                                            <span className="text-[10px] font-bold text-slate-500">
                                                                ₹{c.assets_crore}Cr
                                                            </span>
                                                        </div>
                                                    </div>
                                                ))}
                                            </div>
                                        </div>
                                    )}
                                    
                                    <div className="flex gap-2 mt-4">
                                        <button onClick={handleAnalyze} className="flex-1 bg-gradient-to-r from-blue-600 to-indigo-600 text-white py-3 rounded-xl font-bold text-sm shadow-lg shadow-blue-500/20 hover:shadow-blue-500/40 transition-all flex items-center justify-center gap-2 hover:-translate-y-0.5">
                                            <Sparkles size={16} /> AI Analysis
                                        </button>
                                        <button
                                            onClick={() => setShowComparison(!showComparison)}
                                            className={`flex-1 py-3 rounded-xl font-bold text-sm shadow-lg transition-all flex items-center justify-center gap-2 hover:-translate-y-0.5 ${
                                                showComparison
                                                    ? 'bg-amber-500 text-white shadow-amber-500/20 hover:shadow-amber-500/40'
                                                    : 'bg-gradient-to-r from-slate-700 to-slate-800 text-white shadow-slate-500/20 hover:shadow-slate-500/40'
                                            }`}
                                        >
                                            <BarChart3 size={16} /> {showComparison ? 'Hide' : 'Compare'}
                                        </button>
                                    </div>

                                    <div className="mt-4 pt-4 border-t border-gray-200/50 text-center">
                                        <a href={info.mla_link} target="_blank" className="text-xs font-semibold text-blue-600 hover:underline">
                                            View Official Affidavit Source &rarr;
                                        </a>
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>

                    {/* Ward Comparison Chart (slides in below the card) */}
                    {showComparison && (
                        <div className="mt-3">
                            <WardComparisonChart
                                data={wardStats}
                                onClose={() => setShowComparison(false)}
                                isLoading={isWardStatsLoading}
                            />
                        </div>
                    )}
                </div>
            )}
          </>
      )}
    </div>
  );
}