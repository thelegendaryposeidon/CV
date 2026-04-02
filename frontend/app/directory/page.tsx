"use client";
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Link from 'next/link';
import { 
    ShieldAlert, Wallet, Building2, Search, ArrowLeft, Trophy, Users, 
    ChevronDown, ChevronUp, BarChart3, Sparkles, LayoutDashboard,
    Scale, Globe, TrendingUp
} from 'lucide-react';
import { useRouter } from 'next/navigation';
import { getPartyLogoUrl } from '@/components/partyLogos';
import WardComparisonChart from '@/components/WardComparisonChart';
import AnalysisModal from '@/components/AnalysisModal';
import BetaWarningDialog from '@/components/BetaWarningDialog';

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:8000';
const BETA_ACCEPTED_KEY = "candidatevalidate_beta_accepted";

interface Candidate {
    name: string;
    party: string;
    cases: number;
    assets: string;
    assets_crore: number;
    image?: string;
    is_winner: boolean;
}

interface WardData {
    ward: string;
    winner: Candidate;
    candidates: Candidate[];
    ward_avg: { cases: number; assets_crore: number };
    local_ward_avg: { cases: number; assets_crore: number };
    all_wards_count: number;
}

export default function DirectoryPage() {
    const router = useRouter();
    const [wards, setWards] = useState<WardData[]>([]);
    const [loading, setLoading] = useState(true);
    const [searchQuery, setSearchQuery] = useState('');
    const [expandedWards, setExpandedWards] = useState<Record<string, boolean>>({});
    const [showCharts, setShowCharts] = useState<Record<string, boolean>>({});
    const [showBetaWarning, setShowBetaWarning] = useState(false);
    
    // AI States
    const [isAnalysisOpen, setIsAnalysisOpen] = useState(false);
    const [aiData, setAiData] = useState<any>(null);
    const [isAiLoading, setIsAiLoading] = useState(false);

    useEffect(() => {
        // Check for beta acceptance
        if (typeof window !== "undefined" && !sessionStorage.getItem(BETA_ACCEPTED_KEY)) {
            setShowBetaWarning(true);
        }

        const fetchData = async () => {
            try {
                const res = await axios.get(`${API_BASE}/api/all-candidates`);
                setWards(res.data);
            } catch (error) {
                console.error("Failed to fetch candidates", error);
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, []);

    const filteredWards = wards.filter(w => {
        const q = searchQuery.toLowerCase();
        if (w.ward.toLowerCase().includes(q)) return true;
        if (w.winner.name.toLowerCase().includes(q)) return true;
        if (w.winner.party.toLowerCase().includes(q)) return true;
        return w.candidates.some(c => c.name.toLowerCase().includes(q) || c.party.toLowerCase().includes(q));
    });

    // --- Statistics Calculations ---
    const totalWards = wards.length;
    const totalCandidates = wards.reduce((acc, w) => acc + 1 + w.candidates.length, 0);
    const avgCases = wards.length > 0 ? (wards.reduce((acc, w) => acc + w.winner.cases, 0) / wards.length).toFixed(1) : 0;
    const avgAssets = wards.length > 0 ? (wards.reduce((acc, w) => acc + w.winner.assets_crore, 0) / wards.length).toFixed(1) : 0;

    const getPartyColor = (party: string) => {
        if (!party) return "bg-gray-100 border-gray-300";
        const p = party.toLowerCase();
        if (p.includes("shiv sena") || p.includes("bjp")) return "bg-orange-50 border-orange-200 text-orange-900";
        if (p.includes("congress") || p.includes("ncp")) return "bg-blue-50 border-blue-200 text-blue-900";
        return "bg-emerald-50 border-emerald-200 text-emerald-900"; 
    };

    const toggleWard = (wardName: string) => {
        setExpandedWards(prev => ({ ...prev, [wardName]: !prev[wardName] }));
    };

    const toggleChart = (wardName: string) => {
        setShowCharts(prev => ({ ...prev, [wardName]: !prev[wardName] }));
    };

    const handleAnalyze = async (candidate: Candidate) => {
        setIsAnalysisOpen(true);
        setIsAiLoading(true);
        setAiData(null);
        try {
            const response = await axios.post(`${API_BASE}/api/analyze`, {
                name: candidate.name,
                party: candidate.party,
                cases: String(candidate.cases),
                assets: candidate.assets
            });
            setAiData(response.data);
        } catch (e) { 
            console.error(e);
        } finally { 
            setIsAiLoading(false); 
        }
    };

    const handleAcceptBeta = () => {
        if (typeof window !== "undefined") {
            sessionStorage.setItem(BETA_ACCEPTED_KEY, "true");
        }
        setShowBetaWarning(false);
    };

    const handleCloseBeta = () => {
        setShowBetaWarning(false);
        router.push("/");
    };

    return (
        <div className="min-h-screen bg-[#f8fafc] font-sans text-slate-900 selection:bg-blue-100">
            {/* Mesh Gradient Background Decorative */}
            <div className="fixed inset-0 pointer-events-none opacity-40 z-0 overflow-hidden">
                <div className="absolute -top-[10%] -left-[10%] w-[40%] h-[40%] rounded-full bg-blue-200 blur-[120px] animate-pulse"></div>
                <div className="absolute top-[40%] -right-[5%] w-[30%] h-[30%] rounded-full bg-indigo-100 blur-[100px]"></div>
            </div>

            {/* Header */}
            <header className="sticky top-0 z-40 bg-white/70 backdrop-blur-xl border-b border-slate-200/50 transition-all duration-300 shadow-sm">
                <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
                    <div className="flex items-center gap-5">
                        <Link href="/" className="group p-2.5 hover:bg-slate-100/80 rounded-2xl transition-all border border-transparent hover:border-slate-200">
                            <ArrowLeft size={20} className="text-slate-600 group-hover:-translate-x-1 transition-transform" />
                        </Link>
                        <div>
                            <h1 className="text-2xl font-black tracking-tight text-slate-900 flex items-center gap-2">
                                <Globe className="text-blue-600" size={24} />
                                Candidate<span className="text-blue-600">Directory</span>
                            </h1>
                            <p className="text-[10px] text-slate-400 font-bold tracking-[0.1em] uppercase">Democratic Audit • Maharashtra 2024</p>
                        </div>
                    </div>
                </div>
            </header>

            <main className="relative z-10 max-w-7xl mx-auto px-6 py-10">
                
                {/* Dashboard Stats Row */}
                {!loading && wards.length > 0 && (
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-10">
                        {[
                            { label: "Wards Found", val: totalWards, icon: Building2, color: "text-blue-600", bg: "bg-blue-50" },
                            { label: "Candidates", val: totalCandidates, icon: Users, color: "text-indigo-600", bg: "bg-indigo-50" },
                            { label: "Avg Cases", val: avgCases, icon: ShieldAlert, color: "text-rose-600", bg: "bg-rose-50" },
                            { label: "Avg Assets", val: `₹${avgAssets} Cr`, icon: TrendingUp, color: "text-emerald-600", bg: "bg-emerald-50" },
                        ].map((stat, i) => (
                            <div key={i} className="bg-white/80 p-5 rounded-3xl border border-white shadow-sm backdrop-blur-sm group hover:shadow-md transition-all">
                                <div className={`w-10 h-10 ${stat.bg} ${stat.color} rounded-2xl flex items-center justify-center mb-3 group-hover:scale-110 transition-transform`}>
                                    <stat.icon size={20} />
                                </div>
                                <p className="text-2xl font-black text-slate-900">{stat.val}</p>
                                <p className="text-[10px] font-bold text-slate-400 uppercase tracking-widest">{stat.label}</p>
                            </div>
                        ))}
                    </div>
                )}

                {/* Search Bar - Glassmorphism */}
                <div className="mb-12 max-w-3xl">
                    <div className="relative group">
                        <div className="absolute inset-0 bg-blue-600/5 blur-2xl group-focus-within:bg-blue-600/10 transition-all rounded-3xl"></div>
                        <div className="relative flex items-center">
                            <input
                                type="text"
                                placeholder="Search by Ward, Candidate, or political party..."
                                value={searchQuery}
                                onChange={(e) => setSearchQuery(e.target.value)}
                                className="w-full pl-14 pr-6 py-5 rounded-3xl border border-slate-200 bg-white/90 backdrop-blur-lg shadow-xl shadow-slate-200/20 focus:ring-4 focus:ring-blue-500/10 focus:border-blue-500 outline-none transition-all text-lg font-semibold text-slate-800 placeholder:text-slate-400 placeholder:font-medium"
                            />
                            <Search className="absolute left-5 text-slate-400 group-focus-within:text-blue-600 transition-colors" size={24} />
                        </div>
                    </div>
                </div>

                {loading ? (
                    /* SKELETON LOADING */
                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                        {[1, 2, 3, 4].map(i => (
                            <div key={i} className="bg-white/50 rounded-[2.5rem] border border-slate-200 h-[400px] animate-pulse"></div>
                        ))}
                    </div>
                ) : (
                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-10 items-start">
                        {filteredWards.map((w, idx) => {
                            const isExpanded = expandedWards[w.ward] || false;
                            const isChartOpen = showCharts[w.ward] || false;
                            
                            return (
                                <div key={idx} className="bg-white rounded-[2.5rem] shadow-xl shadow-slate-200/40 border border-slate-100 overflow-hidden flex flex-col group/card hover:-translate-y-1.5 transition-all duration-500">
                                    {/* Ward Info Header */}
                                    <div className="bg-slate-900 px-8 py-6 flex items-center justify-between shrink-0 relative overflow-hidden">
                                        <div className="absolute right-0 top-0 w-24 h-24 bg-blue-500/10 blur-3xl rounded-full translate-x-12 -translate-y-12"></div>
                                        <div className="flex items-center gap-3 relative z-10">
                                            <div className="w-10 h-10 bg-white/10 rounded-2xl flex items-center justify-center text-blue-400 backdrop-blur-sm">
                                                <Building2 size={20} />
                                            </div>
                                            <div>
                                                <h2 className="text-xl font-bold tracking-tight text-white">{w.ward}</h2>
                                                <p className="text-[10px] text-blue-400/80 font-bold uppercase tracking-wider">Assembly Constituency</p>
                                            </div>
                                        </div>
                                        <button 
                                            onClick={() => toggleChart(w.ward)}
                                            className={`relative z-10 flex items-center gap-2 px-4 py-2.5 rounded-2xl text-xs font-bold transition-all shadow-lg ${
                                                isChartOpen 
                                                    ? 'bg-amber-500 text-white shadow-amber-500/40 scale-105' 
                                                    : 'bg-white/10 text-blue-200 hover:bg-white/20 shadow-none'
                                            }`}
                                        >
                                            <BarChart3 size={15} /> {isChartOpen ? 'Close Chart' : 'Compare Data'}
                                        </button>
                                    </div>

                                    {/* Winner Card Body */}
                                    <div className={`p-8 border-b border-slate-100 shrink-0 relative ${getPartyColor(w.winner.party)} transition-colors duration-500`}>
                                        <div className="flex items-center gap-2 mb-6">
                                            <span className="flex items-center gap-1.5 text-[10px] font-black bg-white/80 backdrop-blur-sm text-slate-800 px-3 py-1.5 rounded-full uppercase tracking-widest border border-slate-200/50 shadow-sm">
                                                <Trophy size={11} className="text-amber-500" /> Current Winner
                                            </span>
                                        </div>
                                        
                                        <div className="flex items-start gap-6">
                                            <div className="relative">
                                                <div className="w-20 h-20 rounded-3xl overflow-hidden border-4 border-white shadow-2xl shrink-0 bg-white flex items-center justify-center group-hover/card:scale-110 transition-transform duration-500">
                                                    <img src={getPartyLogoUrl(w.winner.party)} alt={w.winner.party} className="w-14 h-14 object-contain transition-all" />
                                                </div>
                                            </div>
                                            
                                            <div className="flex-1">
                                                <h3 className="text-2xl font-black text-slate-900 leading-[1.1] mb-1 group-hover/card:text-blue-700 transition-colors">{w.winner.name}</h3>
                                                <p className="text-sm font-bold text-slate-500">{w.winner.party}</p>
                                                
                                                <div className="flex flex-wrap gap-3 mt-6">
                                                    <div className="flex items-center gap-2 bg-white/80 backdrop-blur-sm text-rose-600 px-4 py-2.5 rounded-2xl text-sm font-black border border-rose-100 shadow-sm">
                                                        <ShieldAlert size={16} />
                                                        {w.winner.cases} Cases
                                                    </div>
                                                    <div className="flex items-center gap-2 bg-white/80 backdrop-blur-sm text-emerald-600 px-4 py-2.5 rounded-2xl text-sm font-black border border-emerald-100 shadow-sm">
                                                        <Wallet size={16} />
                                                        {w.winner.assets}
                                                    </div>
                                                    <button 
                                                        onClick={() => handleAnalyze(w.winner)}
                                                        className="flex items-center gap-2 bg-blue-600 text-white px-4 py-2.5 rounded-2xl text-sm font-black shadow-lg shadow-blue-500/30 hover:shadow-blue-500/50 hover:scale-105 active:scale-95 transition-all"
                                                    >
                                                        <Sparkles size={16} /> AI Review
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    {/* Chart Expandable */}
                                    {isChartOpen && (
                                        <div className="p-6 bg-slate-50/80 backdrop-blur-sm border-b border-slate-200/50 animate-in slide-in-from-top-4 fade-in duration-500">
                                            <WardComparisonChart 
                                                data={w} 
                                                onClose={() => toggleChart(w.ward)} 
                                                isLoading={false} 
                                            />
                                        </div>
                                    )}

                                    {/* Accordion Competitors */}
                                    {w.candidates && w.candidates.length > 0 && (
                                        <div className="bg-white flex-1 flex flex-col">
                                            <button 
                                                onClick={() => toggleWard(w.ward)}
                                                className="w-full px-8 py-5 flex items-center justify-between text-slate-500 hover:text-blue-600 hover:bg-blue-50/30 transition-all group/btn"
                                            >
                                                <span className="text-[11px] font-black uppercase tracking-[0.2em] flex items-center gap-3">
                                                    <Scale size={15} className="text-slate-400 group-hover/btn:text-blue-500 transition-colors" /> 
                                                    Competing Candidates ({w.candidates.length})
                                                </span>
                                                <div className="w-8 h-8 rounded-full border border-slate-200 flex items-center justify-center group-hover/btn:border-blue-200 group-hover/btn:bg-white transition-all">
                                                    {isExpanded ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                                                </div>
                                            </button>

                                            {isExpanded && (
                                                <div className="px-8 pb-8 space-y-4 animate-in slide-in-from-top-4 fade-in duration-500">
                                                    {w.candidates.map((c, i) => (
                                                        <div key={i} className="flex items-center justify-between bg-slate-50/50 border border-slate-100 rounded-3xl p-4 group/item hover:bg-white hover:shadow-xl hover:shadow-slate-200/40 hover:border-blue-100 transition-all duration-300">
                                                            <div className="flex items-center gap-4">
                                                                <div className="w-10 h-10 rounded-2xl bg-white flex items-center justify-center shrink-0 border border-slate-100 shadow-sm group-hover/item:scale-110 transition-transform">
                                                                    <img src={getPartyLogoUrl(c.party)} alt={c.party} className="w-6 h-6 object-contain" />
                                                                </div>
                                                                <div>
                                                                    <p className="text-sm font-bold text-slate-900">{c.name}</p>
                                                                    <p className="text-[10px] text-slate-400 font-bold uppercase tracking-wider">{c.party}</p>
                                                                </div>
                                                            </div>
                                                            <div className="flex items-center gap-3">
                                                                <div className={`px-2.5 py-1 rounded-full font-black text-[10px] uppercase ${
                                                                    c.cases === 0 ? 'bg-emerald-50 text-emerald-600' :
                                                                    c.cases <= 2 ? 'bg-amber-50 text-amber-600' :
                                                                    'bg-rose-50 text-rose-600'
                                                                }`}>
                                                                    {c.cases} Cases
                                                                </div>
                                                                <button 
                                                                    onClick={() => handleAnalyze(c)}
                                                                    className="w-8 h-8 rounded-full bg-slate-100 text-slate-400 flex items-center justify-center hover:bg-blue-600 hover:text-white transition-all shadow-sm"
                                                                >
                                                                    <Sparkles size={14} />
                                                                </button>
                                                            </div>
                                                        </div>
                                                    ))}
                                                </div>
                                            )}
                                        </div>
                                    )}
                                </div>
                            );
                        })}
                    </div>
                )}

                {/* Empty State */}
                {filteredWards.length === 0 && !loading && (
                    <div className="max-w-md mx-auto py-32 text-center animate-in zoom-in duration-500">
                        <div className="inline-flex w-24 h-24 bg-blue-50 text-blue-600 rounded-[2.5rem] items-center justify-center mb-8 shadow-inner shadow-blue-200">
                            <Search className="opacity-50" size={40} />
                        </div>
                        <h3 className="text-3xl font-black text-slate-900 mb-3 tracking-tight">No results found</h3>
                        <p className="text-slate-500 font-medium leading-relaxed">We couldn't find any wards or candidates matching "<span className="text-blue-600 font-bold">{searchQuery}</span>". Try adjusting your filters.</p>
                    </div>
                )}
            </main>

            <footer className="relative z-10 py-20 text-center border-t border-slate-200/50 bg-white/50 backdrop-blur-lg mt-20">
                <p className="text-slate-400 text-[11px] font-black uppercase tracking-[0.3em] mb-4">Official Data Sources: myneta.info • ECI</p>
                <p className="text-slate-900 font-bold mb-2">CandidateValidate v1.0 Beta</p>
                <div className="flex justify-center gap-6 mt-8 opacity-40">
                    <Globe size={18} />
                    <Scale size={18} />
                    <TrendingUp size={18} />
                </div>
            </footer>

            {/* AI Analysis Modal Integration */}
            <AnalysisModal 
                isOpen={isAnalysisOpen} 
                onClose={() => setIsAnalysisOpen(false)} 
                data={aiData} 
                isLoading={isAiLoading} 
            />

            {/* BETA WARNING DIALOG */}
            <BetaWarningDialog 
                isOpen={showBetaWarning} 
                onAccept={handleAcceptBeta} 
                onClose={handleCloseBeta} 
                acceptText="Explore Directory"
            />
        </div>
    );
}
