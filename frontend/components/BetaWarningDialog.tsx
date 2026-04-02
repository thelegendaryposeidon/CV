"use client";
import React, { useState, useEffect } from 'react';
import { AlertTriangle, ExternalLink, CheckCircle2 } from 'lucide-react';

interface BetaWarningDialogProps {
  isOpen: boolean;
  onAccept: () => void;
  onClose: () => void;
  acceptText?: string;
}

export default function BetaWarningDialog({ isOpen, onAccept, onClose, acceptText = "Proceed to Map" }: BetaWarningDialogProps) {
  const [accepted, setAccepted] = useState(false);

  // Reset checkbox when dialog opens
  useEffect(() => {
    if (isOpen) setAccepted(false);
  }, [isOpen]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-[9999] flex items-center justify-center p-4">
      {/* Backdrop */}
      <div 
        className="absolute inset-0 bg-black/60 backdrop-blur-sm"
        onClick={onClose}
      />

      {/* Dialog */}
      <div 
        className="relative bg-white rounded-3xl shadow-2xl max-w-lg w-full overflow-hidden border border-gray-200"
        style={{ animation: 'dialogEnter 0.35s cubic-bezier(0.16, 1, 0.3, 1)' }}
      >
        {/* Top Warning Bar */}
        <div className="bg-gradient-to-r from-amber-500 to-orange-500 px-6 py-4 flex items-center gap-3">
          <div className="bg-white/20 p-2 rounded-xl backdrop-blur-sm">
            <AlertTriangle size={24} className="text-white" strokeWidth={2.5} />
          </div>
          <div>
            <h2 className="text-lg font-black text-white tracking-tight">Beta Version</h2>
            <p className="text-amber-100 text-xs font-semibold">Use With Caution</p>
          </div>
        </div>

        {/* Body */}
        <div className="px-6 py-6">
          <p className="text-slate-700 text-sm leading-relaxed mb-4">
            <strong>CandidateValidate</strong> is currently in <strong>active beta</strong>. 
            All information displayed about candidates and constituencies — including criminal records, 
            assets, and party affiliations — is sourced from publicly available data and may contain 
            inaccuracies or be outdated.
          </p>

          <div className="bg-amber-50 border border-amber-200 rounded-xl p-4 mb-4">
            <p className="text-amber-900 text-sm font-semibold mb-2">
              ⚠️ Please verify any inconsistencies yourself using official sources:
            </p>
            <ul className="space-y-2">
              <li>
                <a 
                  href="https://myneta.info/" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="flex items-center gap-2 text-sm text-blue-600 font-semibold hover:text-blue-800 hover:underline transition-colors"
                >
                  <ExternalLink size={14} />
                  MyNeta.info — Candidate Affidavits
                </a>
              </li>
              <li>
                <a 
                  href="https://eci.gov.in/" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="flex items-center gap-2 text-sm text-blue-600 font-semibold hover:text-blue-800 hover:underline transition-colors"
                >
                  <ExternalLink size={14} />
                  Election Commission of India
                </a>
              </li>
            </ul>
          </div>

          {/* Checkbox */}
          <label className="flex items-start gap-3 cursor-pointer group select-none mb-6">
            <div className="relative mt-0.5">
              <input
                type="checkbox"
                checked={accepted}
                onChange={(e) => setAccepted(e.target.checked)}
                className="sr-only"
              />
              <div className={`w-5 h-5 rounded-md border-2 flex items-center justify-center transition-all duration-200 ${
                accepted 
                  ? 'bg-blue-600 border-blue-600 shadow-lg shadow-blue-500/30' 
                  : 'border-gray-300 group-hover:border-blue-400 bg-white'
              }`}>
                {accepted && <CheckCircle2 size={14} className="text-white" strokeWidth={3} />}
              </div>
            </div>
            <span className="text-slate-600 text-sm leading-snug">
              I understand that this data is in beta and may be inaccurate. I will verify critical information using official sources.
            </span>
          </label>

          {/* Buttons */}
          <div className="flex gap-3">
            <button
              onClick={onClose}
              className="flex-1 px-5 py-3 rounded-xl border border-gray-200 text-slate-600 font-bold text-sm hover:bg-gray-50 transition-all"
            >
              Go Back
            </button>
            <button
              onClick={onAccept}
              disabled={!accepted}
              className={`flex-1 px-5 py-3 rounded-xl font-bold text-sm transition-all flex items-center justify-center gap-2 ${
                accepted
                  ? 'bg-gradient-to-r from-blue-600 to-indigo-600 text-white shadow-lg shadow-blue-500/25 hover:shadow-blue-500/40 hover:-translate-y-0.5'
                  : 'bg-gray-100 text-gray-400 cursor-not-allowed'
              }`}
            >
              {acceptText}
            </button>
          </div>
        </div>

        {/* Animation keyframes */}
        <style jsx>{`
          @keyframes dialogEnter {
            from {
              opacity: 0;
              transform: scale(0.95) translateY(10px);
            }
            to {
              opacity: 1;
              transform: scale(1) translateY(0);
            }
          }
        `}</style>
      </div>
    </div>
  );
}
