/**
 * partyLogos.ts
 * Maps political party names to their corresponding insignia SVG paths.
 * Logos are stored as static SVGs in /party-logos/.
 */

const PARTY_LOGO_MAP: [RegExp, string][] = [
  // Order matters: more specific matches first
  [/shiv\s*sena\s*\(?\s*ubt\s*\)?/i,       '/party-logos/shiv-sena-ubt.svg'],
  [/shiv\s*sena/i,                           '/party-logos/shiv-sena.svg'],
  [/ncp\s*\(?\s*sharad\s*pawar\s*\)?/i,      '/party-logos/ncp-sp.svg'],
  [/ncp\s*\(?\s*sp\s*\)?/i,                  '/party-logos/ncp-sp.svg'],
  [/\bncp\b/i,                               '/party-logos/ncp.svg'],
  [/\bbjp\b/i,                               '/party-logos/bjp.svg'],
  [/\bcongress\b/i,                           '/party-logos/congress.svg'],
  [/\baimim\b/i,                              '/party-logos/aimim.svg'],
  [/\bmns\b/i,                               '/party-logos/mns.svg'],
  [/\b[a]+ap\b/i,                            '/party-logos/aap.svg'],      // AAP or AAAP
  [/samajwadi/i,                              '/party-logos/sp.svg'],
  [/\bsp\b/i,                                '/party-logos/sp.svg'],
  [/\bvba\b|bahujan\s*vikas/i,               '/party-logos/vba.svg'],
  [/\bbsp\b/i,                               '/party-logos/bsp.svg'],
  [/\bcpi\b/i,                               '/party-logos/cpi.svg'],
  [/\bdmk\b/i,                               '/party-logos/dmk.svg'],
  [/independent/i,                            '/party-logos/independent.svg'],
];

/**
 * Returns the URL path to the party's insignia SVG.
 * Falls back to a generic flag icon if the party is unrecognised.
 */
export function getPartyLogoUrl(party: string | undefined | null): string {
  if (!party) return '/party-logos/default.svg';

  for (const [pattern, path] of PARTY_LOGO_MAP) {
    if (pattern.test(party)) return path;
  }

  return '/party-logos/default.svg';
}
