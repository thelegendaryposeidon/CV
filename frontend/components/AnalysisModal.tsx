import React from 'react';
import { X } from 'lucide-react';

export default function AnalysisModal({ isOpen, onClose, data, isLoading }: any) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-in fade-in">
      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-md overflow-hidden">
        <div className="bg-slate-900 text-white p-4 flex justify-between items-center">
          <h3 className="font-bold flex gap-2"><span className="bg-blue-600 px-1 rounded text-xs uppercase">AI Report</span> Analysis</h3>
          <button onClick={onClose}><X size={18}/></button>
        </div>
        <div className="p-6">
          {isLoading ? (
            <div className="text-center py-8">
              <div className="w-8 h-8 border-4 border-blue-600 border-t-transparent rounded-full animate-spin mx-auto mb-4"/>
              <p className="text-slate-500">Consulting Gemini...</p>
            </div>
          ) : data ? (
            <div className="space-y-4">
               <div className="text-center">
                <span className={`px-4 py-1 rounded-full font-bold uppercase text-sm border ${
                    data.verdict === 'Safe' ? 'bg-green-100 text-green-700 border-green-200' : 
                    data.verdict === 'Risky' ? 'bg-red-100 text-red-700 border-red-200' : 
                    'bg-amber-100 text-amber-700 border-amber-200'
                }`}>Verdict: {data.verdict}</span>
               </div>
               <p className="text-sm text-slate-600 italic bg-slate-50 p-3 rounded border">"{data.summary}"</p>
               <div className="grid grid-cols-2 gap-2 text-xs">
                 <div><b className="text-red-500">RED FLAGS</b>{data.red_flags?.map((f:any, i:number)=><div key={i}>• {f}</div>)}</div>
                 <div><b className="text-green-500">GREEN FLAGS</b>{data.green_flags?.map((f:any, i:number)=><div key={i}>• {f}</div>)}</div>
               </div>
            </div>
          ) : <p className="text-red-500 text-center">Analysis Failed.</p>}
        </div>
      </div>
    </div>
  );
}