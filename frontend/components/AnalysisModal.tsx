import React from 'react';
import { X } from 'lucide-react';
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip,
  ResponsiveContainer, Cell
} from 'recharts';

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

               {data.candidate_stats && data.state_avg && (
                 <div className="mt-4 pt-4 border-t border-slate-100">
                   <h4 className="text-[10px] font-black uppercase tracking-widest text-slate-400 mb-3">Statewide Comparison Baseline</h4>
                   
                   <div className="space-y-4">
                     {/* Criminal Cases Comparison Chart */}
                     <div>
                       <h4 className="text-[10px] font-bold uppercase tracking-wider text-slate-400 mb-2 flex items-center gap-1.5">
                         <span className="w-2 h-2 rounded-full bg-rose-400 inline-block" />
                         Criminal Cases Declared
                       </h4>
                       <div className="bg-slate-50/50 rounded-xl border border-slate-100 p-2">
                         <ResponsiveContainer width="100%" height={100}>
                           <BarChart 
                             data={[
                               { name: 'Candidate', value: data.candidate_stats.cases },
                               { name: 'State Avg', value: data.state_avg.cases }
                             ]} 
                             layout="vertical"
                             margin={{ top: 5, right: 20, left: 10, bottom: 5 }} 
                           >
                             <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" horizontal={false} />
                             <XAxis type="number" tick={{ fontSize: 10, fill: '#94a3b8' }} axisLine={false} tickLine={false} allowDecimals={false} />
                             <YAxis dataKey="name" type="category" tick={{ fontSize: 10, fill: '#64748b', fontWeight: 600 }} axisLine={false} tickLine={false} width={65} />
                             <Tooltip 
                               cursor={{ fill: 'rgba(244,63,94,0.06)' }} 
                               contentStyle={{ borderRadius: '8px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)', fontSize: '12px', fontWeight: 'bold' }} 
                             />
                             <Bar dataKey="value" name="Cases" radius={[0, 4, 4, 0]} barSize={20}>
                               <Cell fill="#f43f5e" /> {/* Rose for candidate */}
                               <Cell fill="#94a3b8" /> {/* Slate for average */}
                             </Bar>
                           </BarChart>
                         </ResponsiveContainer>
                       </div>
                     </div>

                     {/* Assets Comparison Chart */}
                     <div>
                       <h4 className="text-[10px] font-bold uppercase tracking-wider text-slate-400 mb-2 flex items-center gap-1.5">
                         <span className="w-2 h-2 rounded-full bg-emerald-400 inline-block" />
                         Declared Assets (₹ Crore)
                       </h4>
                       <div className="bg-slate-50/50 rounded-xl border border-slate-100 p-2">
                         <ResponsiveContainer width="100%" height={100}>
                           <BarChart 
                             data={[
                               { name: 'Candidate', value: data.candidate_stats.assets_crore },
                               { name: 'State Avg', value: data.state_avg.assets_crore }
                             ]} 
                             layout="vertical"
                             margin={{ top: 5, right: 20, left: 10, bottom: 5 }} 
                           >
                             <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" horizontal={false} />
                             <XAxis type="number" tick={{ fontSize: 10, fill: '#94a3b8' }} axisLine={false} tickLine={false} />
                             <YAxis dataKey="name" type="category" tick={{ fontSize: 10, fill: '#64748b', fontWeight: 600 }} axisLine={false} tickLine={false} width={65} />
                             <Tooltip 
                               cursor={{ fill: 'rgba(16,185,129,0.06)' }} 
                               contentStyle={{ borderRadius: '8px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)', fontSize: '12px', fontWeight: 'bold' }} 
                             />
                             <Bar dataKey="value" name="Assets (₹ Cr)" radius={[0, 4, 4, 0]} barSize={20}>
                               <Cell fill="#10b981" /> {/* Emerald for candidate */}
                               <Cell fill="#94a3b8" /> {/* Slate for average */}
                             </Bar>
                           </BarChart>
                         </ResponsiveContainer>
                       </div>
                     </div>
                   </div>
                 </div>
               )}
            </div>
          ) : <p className="text-red-500 text-center">Analysis Failed.</p>}
        </div>
      </div>
    </div>
  );
}