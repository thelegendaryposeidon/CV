"use client";
import { useState, useEffect } from "react";
import MapInterface from "@/components/MapInterface";
import BetaWarningDialog from "@/components/BetaWarningDialog";

const BETA_ACCEPTED_KEY = "candidatevalidate_beta_accepted";

export default function MapPage() {
  const [betaAccepted, setBetaAccepted] = useState<boolean | null>(null);

  useEffect(() => {
    // Check if user already accepted this session
    const accepted = sessionStorage.getItem(BETA_ACCEPTED_KEY);
    setBetaAccepted(!!accepted);
  }, []);

  const handleAccept = () => {
    sessionStorage.setItem(BETA_ACCEPTED_KEY, "true");
    setBetaAccepted(true);
  };

  const handleClose = () => {
    // Go back to the previous page (or home)
    window.history.back();
  };

  // Show nothing while checking sessionStorage (avoids flash)
  if (betaAccepted === null) {
    return null;
  }

  return (
    <main className="h-screen w-screen overflow-hidden">
      {betaAccepted ? (
        <MapInterface />
      ) : (
        <>
          {/* Show a blurred/dimmed map preview behind the dialog */}
          <div className="opacity-20 blur-sm pointer-events-none">
            <MapInterface isPreview={true} />
          </div>
          <BetaWarningDialog
            isOpen={true}
            onAccept={handleAccept}
            onClose={handleClose}
          />
        </>
      )}
    </main>
  );
}