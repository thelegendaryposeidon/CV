"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import Image from "next/image";
import { Map, ArrowRight, Search, ShieldAlert, FileText, Users } from "lucide-react";
import MapInterface from "@/components/MapInterface"; 
import BetaWarningDialog from "@/components/BetaWarningDialog";

const BETA_ACCEPTED_KEY = "candidatevalidate_beta_accepted";

export default function Home() {
  const [showBetaWarning, setShowBetaWarning] = useState(false);
  const router = useRouter();

  const handleMapClick = (e: React.MouseEvent) => {
    e.preventDefault();
    // If already accepted this session, go straight to map
    if (typeof window !== "undefined" && sessionStorage.getItem(BETA_ACCEPTED_KEY)) {
      router.push("/map");
      return;
    }
    setShowBetaWarning(true);
  };

  const handleAccept = () => {
    if (typeof window !== "undefined") {
      sessionStorage.setItem(BETA_ACCEPTED_KEY, "true");
    }
    setShowBetaWarning(false);
    router.push("/map");
  };

  return (
    <div className="min-h-screen bg-white font-sans text-slate-900 selection:bg-blue-100 selection:text-blue-900">
      
      <div className="fixed inset-0 z-0 opacity-40 pointer-events-none" 
           style={{ backgroundImage: 'radial-gradient(#cbd5e1 1px, transparent 1px)', backgroundSize: '24px 24px' }}>
      </div>

      {/* NAVBAR */}
      <nav className="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-gray-200/50 supports-[backdrop-filter]:bg-white/60">
        <div className="max-w-7xl mx-auto px-6 h-20 flex justify-between items-center">
          
          <Link href="/" className="flex items-center gap-2.5 hover:opacity-80 transition-opacity">
            <Image
              src="/logo.png"
              alt="CandidateValidate Logo"
              width={40}
              height={40}
              className="rounded-lg shadow-lg shadow-blue-500/30"
              priority
            />
            <span className="text-2xl font-black tracking-tight text-slate-900">
              Candidate<span className="text-blue-600">Validate</span>
            </span>
          </Link>
          
          <div className="hidden md:flex items-center gap-8 font-semibold text-sm text-slate-600">
            <a href="/map" onClick={handleMapClick} className="hover:text-blue-600 transition-colors cursor-pointer">Live Map</a>
            
            <Link 
              href="/directory" 
              className="hover:text-blue-600 transition-colors"
            >
              Candidate Directory
            </Link>
            
            <Link 
              href="https://myneta.info/" 
              target="_blank" 
              className="hover:text-blue-600 transition-colors"
            >
              Data Sources
            </Link>
            
            <a 
              href="/map"
              onClick={handleMapClick}
              className="bg-slate-900 text-white px-6 py-2.5 rounded-full hover:bg-slate-800 transition-all shadow-xl hover:shadow-2xl hover:-translate-y-0.5 flex items-center gap-2 group cursor-pointer"
            >
              Launch App <ArrowRight size={16} className="group-hover:translate-x-1 transition-transform" />
            </a>
          </div>
        </div>
      </nav>

      {/* HERO SECTION */}
      <section className="relative z-10 pt-24 pb-32 px-6">
        <div className="max-w-5xl mx-auto text-center">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-blue-50 border border-blue-100 text-blue-700 text-xs font-bold uppercase tracking-widest mb-8 animate-in fade-in slide-in-from-bottom-4 duration-700">
            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
            </span>
            Live Maharashtra Election Data
          </div>
          
          <h1 className="text-6xl md:text-8xl font-black text-slate-900 mb-8 tracking-tighter leading-[0.9]">
            Democracy <br className="hidden md:block" />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600">
              Needs Validation.
            </span>
          </h1>
          
          <p className="text-xl md:text-2xl text-slate-500 max-w-2xl mx-auto mb-12 leading-relaxed font-medium">
            Don't vote in the dark. Instantly verify criminal records, assets, and performance of your candidates with one click.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <a href="/map" onClick={handleMapClick} className="w-full sm:w-auto px-8 py-4 bg-blue-600 text-white rounded-2xl font-bold text-lg hover:bg-blue-700 transition-all shadow-xl shadow-blue-500/20 hover:shadow-blue-500/40 hover:-translate-y-1 flex items-center justify-center gap-2 cursor-pointer">
              <Search size={20} /> Find My Constituency
            </a>
            <Link href="/directory" className="w-full sm:w-auto px-8 py-4 bg-white text-blue-600 border-2 border-blue-600 rounded-2xl font-bold text-lg hover:bg-blue-50 transition-all shadow-xl hover:-translate-y-1 flex items-center justify-center gap-2 cursor-pointer">
              <Users size={20} /> View Candidate Directory
            </Link>
          </div>

          <div className="relative mt-20 hidden md:block">
             <div className="mx-auto max-w-4xl bg-white rounded-xl shadow-2xl border border-slate-200 overflow-hidden">
                <div className="bg-slate-50 border-b border-slate-200 px-4 py-3 flex gap-2">
                    <div className="w-3 h-3 rounded-full bg-red-400"></div>
                    <div className="w-3 h-3 rounded-full bg-amber-400"></div>
                    <div className="w-3 h-3 rounded-full bg-green-400"></div>
                </div>
                
                <div className="aspect-[16/7] bg-slate-100 relative overflow-hidden flex items-center justify-center group">
                    <div className="absolute inset-0 z-0">
                        <MapInterface isPreview={true} />
                    </div>

                    <div className="absolute inset-0 bg-black/5 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity z-10 backdrop-blur-[2px]">
                        <a href="/map" onClick={handleMapClick} className="bg-white text-slate-900 px-6 py-3 rounded-full font-bold shadow-xl flex items-center gap-2 transform translate-y-4 group-hover:translate-y-0 transition-all duration-300 cursor-pointer">
                            <Map size={18} /> Explore Full Map
                        </a>
                    </div>

                </div>
             </div>
          </div>
        </div>
      </section>

      {/* --- NEW FEATURES SECTION --- */}
      <section className="relative z-10 py-24 bg-white border-t border-slate-100">
        <div className="max-w-7xl mx-auto px-6">
          <div className="grid md:grid-cols-3 gap-8">
            
            {/* Feature 1: Map (Keep) */}
            <div className="bg-slate-50 p-8 rounded-3xl border border-slate-100 hover:border-blue-200 hover:shadow-lg hover:shadow-blue-500/5 transition-all group">
              <div className="w-14 h-14 bg-white rounded-2xl flex items-center justify-center shadow-sm text-blue-600 mb-6 group-hover:scale-110 transition-transform duration-300">
                <Map size={28} />
              </div>
              <h3 className="text-xl font-bold text-slate-900 mb-3">Precision Mapping</h3>
              <p className="text-slate-500 leading-relaxed">
                We use advanced geospatial data to pinpoint your exact administrative ward. No more guessing boundaries.
              </p>
            </div>

            {/* Feature 2: Criminal Check (New) */}
            <div className="bg-slate-50 p-8 rounded-3xl border border-slate-100 hover:border-red-200 hover:shadow-lg hover:shadow-red-500/5 transition-all group">
              <div className="w-14 h-14 bg-white rounded-2xl flex items-center justify-center shadow-sm text-red-600 mb-6 group-hover:scale-110 transition-transform duration-300">
                <ShieldAlert size={28} />
              </div>
              <h3 className="text-xl font-bold text-slate-900 mb-3">Criminal Record Check</h3>
              <p className="text-slate-500 leading-relaxed">
                Transparency first. Instantly spot candidates with declared criminal cases and analyzing seriousness before you vote.
              </p>
            </div>

            {/* Feature 3: Official Docs (New) */}
            <div className="bg-slate-50 p-8 rounded-3xl border border-slate-100 hover:border-green-200 hover:shadow-lg hover:shadow-green-500/5 transition-all group">
              <div className="w-14 h-14 bg-white rounded-2xl flex items-center justify-center shadow-sm text-green-600 mb-6 group-hover:scale-110 transition-transform duration-300">
                <FileText size={28} />
              </div>
              <h3 className="text-xl font-bold text-slate-900 mb-3">Official Affidavit Access</h3>
              <p className="text-slate-500 leading-relaxed">
                Verify the truth yourself. We provide deep-links to the original signed affidavits on the Election Commission portal.
              </p>
            </div>

          </div>
        </div>
      </section>

      <footer className="py-12 text-center text-slate-400 text-sm font-medium border-t border-slate-100">
        <p>Built for Mumbai Hacks 2026 • Powering Informed Democracy</p>
      </footer>

      {/* BETA WARNING DIALOG */}
      <BetaWarningDialog 
        isOpen={showBetaWarning} 
        onAccept={handleAccept} 
        onClose={() => setShowBetaWarning(false)} 
      />
    </div>
  );
}