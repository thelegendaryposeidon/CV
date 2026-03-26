"use client";
import React from 'react';
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip,
  ResponsiveContainer, ReferenceLine, Cell,
} from 'recharts';
import { Trophy, X } from 'lucide-react';

interface Candidate {
  name: string;
  party: string;
  cases: number;
  assets_crore: number;
  is_winner: boolean;
}

interface WardStatsData {
  ward: string;
  winner: Candidate;
  candidates: Candidate[];
  ward_avg: { cases: number; assets_crore: number };
  local_ward_avg: { cases: number; assets_crore: number };
  all_wards_count: number;
}

interface WardComparisonChartProps {
  data: WardStatsData | null;
  onClose: () => void;
  isLoading: boolean;
}

/* Truncate long names for bar labels */
const shortName = (name: string, max = 12) =>
  name.length > max ? name.slice(0, max - 1) + '…' : name;

/* Get party-based bar colour */
const partyColor = (party: string, isWinner: boolean): string => {
  if (isWinner) return '#f59e0b'; // amber / gold for winner
  const p = party.toLowerCase();
  if (p.includes('bjp')) return '#f97316';
  if (p.includes('congress')) return '#3b82f6';
  if (p.includes('shiv sena') && p.includes('ubt')) return '#ef4444';
  if (p.includes('shiv sena')) return '#fb923c';
  if (p.includes('ncp') && p.includes('sp')) return '#6366f1';
  if (p.includes('ncp')) return '#06b6d4';
  if (p.includes('aimim')) return '#10b981';
  if (p.includes('mns')) return '#ec4899';
  if (p.includes('independent')) return '#64748b';
  return '#94a3b8';
};

/* Custom tooltip */
const ChartTooltip = ({ active, payload, label }: any) => {
  if (!active || !payload?.length) return null;
  const d = payload[0]?.payload;
  return (
    <div className="bg-white/95 backdrop-blur-sm px-4 py-3 rounded-xl shadow-xl border border-gray-100 text-xs max-w-[220px]">
      <p className="font-bold text-slate-800 text-sm mb-1">{d?.fullName || label}</p>
      <p className="text-slate-500 mb-2">{d?.party}</p>
      {payload.map((entry: any, i: number) => (
        <div key={i} className="flex justify-between gap-4">
          <span className="text-slate-500">{entry.name}</span>
          <span className="font-bold" style={{ color: entry.color }}>{entry.value}</span>
        </div>
      ))}
      {d?.is_winner && (
        <div className="mt-2 flex items-center gap-1 text-amber-600 font-bold">
          <Trophy size={12} /> Winner
        </div>
      )}
    </div>
  );
};

export default function WardComparisonChart({ data, onClose, isLoading }: WardComparisonChartProps) {
  if (!data && !isLoading) return null;

  /* Build unified dataset: winner first, then aspirants */
  const allCandidates: (Candidate & { label: string; fullName: string })[] = [];
  if (data) {
    allCandidates.push({
      ...data.winner,
      label: shortName(data.winner.name) + ' ★',
      fullName: data.winner.name,
    });
    data.candidates.forEach((c) => {
      allCandidates.push({ ...c, label: shortName(c.name), fullName: c.name });
    });
  }

  return (
    <div className="bg-white rounded-2xl shadow-2xl border border-gray-100 overflow-hidden animate-in slide-in-from-bottom-4 fade-in duration-500">
      {/* Header */}
      <div className="bg-gradient-to-r from-slate-900 via-slate-800 to-slate-900 text-white px-5 py-3.5 flex justify-between items-center">
        <div className="flex items-center gap-2">
          <span className="text-[10px] font-bold uppercase tracking-widest bg-amber-500/20 text-amber-300 px-2 py-0.5 rounded">
            Ward Comparison
          </span>
          {data && (
            <span className="text-sm font-semibold text-white/80">{data.ward}</span>
          )}
        </div>
        <button
          onClick={onClose}
          className="text-white/50 hover:text-white transition-colors p-1 rounded-lg hover:bg-white/10"
        >
          <X size={16} />
        </button>
      </div>

      {isLoading ? (
        <div className="p-10 text-center">
          <div className="w-8 h-8 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mx-auto mb-3" />
          <p className="text-slate-500 text-sm font-medium">Loading ward statistics…</p>
        </div>
      ) : data ? (
        <div className="p-4 space-y-5">
          {/* Ward Average Banner */}
          <div className="flex gap-3 text-xs">
            <div className="flex-1 bg-blue-50 border border-blue-100 rounded-xl px-3 py-2.5 text-center">
              <p className="text-blue-400 font-bold uppercase tracking-wider text-[10px] mb-0.5">Mumbai Avg Cases</p>
              <p className="text-blue-700 font-black text-lg">{data.ward_avg.cases}</p>
            </div>
            <div className="flex-1 bg-emerald-50 border border-emerald-100 rounded-xl px-3 py-2.5 text-center">
              <p className="text-emerald-400 font-bold uppercase tracking-wider text-[10px] mb-0.5">Mumbai Avg Assets</p>
              <p className="text-emerald-700 font-black text-lg">₹{data.ward_avg.assets_crore} Cr</p>
            </div>
            <div className="flex-1 bg-slate-50 border border-slate-100 rounded-xl px-3 py-2.5 text-center">
              <p className="text-slate-400 font-bold uppercase tracking-wider text-[10px] mb-0.5">Wards Analyzed</p>
              <p className="text-slate-700 font-black text-lg">{data.all_wards_count}</p>
            </div>
          </div>

          {/* CHART 1: Criminal Cases */}
          <div>
            <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2 flex items-center gap-1.5">
              <span className="w-2 h-2 rounded-full bg-red-400 inline-block" />
              Criminal Cases Declared
            </h4>
            <div className="bg-slate-50/50 rounded-xl border border-slate-100 p-2">
              <ResponsiveContainer width="100%" height={180}>
                <BarChart data={allCandidates} margin={{ top: 10, right: 10, left: -15, bottom: 5 }} barCategoryGap="20%">
                  <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" vertical={false} />
                  <XAxis
                    dataKey="label"
                    tick={{ fontSize: 10, fill: '#64748b', fontWeight: 600 }}
                    axisLine={false}
                    tickLine={false}
                  />
                  <YAxis
                    tick={{ fontSize: 10, fill: '#94a3b8' }}
                    axisLine={false}
                    tickLine={false}
                    allowDecimals={false}
                  />
                  <Tooltip content={<ChartTooltip />} cursor={{ fill: 'rgba(59,130,246,0.06)' }} />
                  <ReferenceLine
                    y={data.ward_avg.cases}
                    stroke="#3b82f6"
                    strokeDasharray="6 4"
                    strokeWidth={2}
                    label={{
                      value: `Mumbai Avg: ${data.ward_avg.cases}`,
                      position: 'insideTopRight',
                      fontSize: 10,
                      fill: '#3b82f6',
                      fontWeight: 700,
                    }}
                    />
                  <ReferenceLine
                    y={data.local_ward_avg.cases}
                    stroke="#8b5cf6"
                    strokeDasharray="3 3"
                    strokeWidth={2}
                    label={{
                      value: `Ward Avg: ${data.local_ward_avg.cases}`,
                      position: 'insideTopLeft',
                      fontSize: 10,
                      fill: '#8b5cf6',
                      fontWeight: 700,
                    }}
                  />
                  <Bar dataKey="cases" name="Cases" radius={[6, 6, 0, 0]} maxBarSize={44}>
                    {allCandidates.map((c, i) => (
                      <Cell key={i} fill={partyColor(c.party, c.is_winner)} fillOpacity={c.is_winner ? 1 : 0.75} />
                    ))}
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* CHART 2: Declared Assets */}
          <div>
            <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2 flex items-center gap-1.5">
              <span className="w-2 h-2 rounded-full bg-emerald-400 inline-block" />
              Declared Assets (₹ Crore)
            </h4>
            <div className="bg-slate-50/50 rounded-xl border border-slate-100 p-2">
              <ResponsiveContainer width="100%" height={180}>
                <BarChart data={allCandidates} margin={{ top: 10, right: 10, left: -15, bottom: 5 }} barCategoryGap="20%">
                  <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" vertical={false} />
                  <XAxis
                    dataKey="label"
                    tick={{ fontSize: 10, fill: '#64748b', fontWeight: 600 }}
                    axisLine={false}
                    tickLine={false}
                  />
                  <YAxis
                    tick={{ fontSize: 10, fill: '#94a3b8' }}
                    axisLine={false}
                    tickLine={false}
                  />
                  <Tooltip content={<ChartTooltip />} cursor={{ fill: 'rgba(16,185,129,0.06)' }} />
                  <ReferenceLine
                    y={data.ward_avg.assets_crore}
                    stroke="#10b981"
                    strokeDasharray="6 4"
                    strokeWidth={2}
                    label={{
                      value: `Mumbai Avg: ₹${data.ward_avg.assets_crore} Cr`,
                      position: 'insideTopRight',
                      fontSize: 10,
                      fill: '#10b981',
                      fontWeight: 700,
                    }}
                    />
                  <ReferenceLine
                    y={data.local_ward_avg.assets_crore}
                    stroke="#8b5cf6"
                    strokeDasharray="3 3"
                    strokeWidth={2}
                    label={{
                      value: `Ward Avg: ₹${data.local_ward_avg.assets_crore} Cr`,
                      position: 'insideTopLeft',
                      fontSize: 10,
                      fill: '#8b5cf6',
                      fontWeight: 700,
                    }}
                  />
                  <Bar dataKey="assets_crore" name="Assets (₹ Cr)" radius={[6, 6, 0, 0]} maxBarSize={44}>
                    {allCandidates.map((c, i) => (
                      <Cell key={i} fill={partyColor(c.party, c.is_winner)} fillOpacity={c.is_winner ? 1 : 0.75} />
                    ))}
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* Legend */}
          <div className="flex flex-wrap items-center gap-x-4 gap-y-1 text-[10px] text-slate-500 font-medium pt-1 border-t border-slate-100">
            <div className="flex items-center gap-1">
              <span className="w-3 h-3 rounded bg-amber-400 inline-block" />
              <span>Winner ★</span>
            </div>
            <div className="flex items-center gap-1">
              <span className="w-3 h-1 bg-blue-500 inline-block rounded" style={{ borderTop: '2px dashed #3b82f6' }} />
              <span>Mumbai Avg (Cases)</span>
            </div>
            <div className="flex items-center gap-1">
              <span className="w-3 h-1 bg-emerald-500 inline-block rounded" style={{ borderTop: '2px dashed #10b981' }} />
              <span>Mumbai Avg (Assets)</span>
            </div>
            <div className="flex items-center gap-1">
              <span className="w-3 h-1 bg-violet-500 inline-block rounded" style={{ borderTop: '2px dashed #8b5cf6' }} />
              <span>Ward Avg</span>
            </div>
            <span className="ml-auto text-slate-400 italic">Bars colored by party</span>
          </div>
        </div>
      ) : null}
    </div>
  );
}
