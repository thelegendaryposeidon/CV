import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css"; // Ensure this import is here for Tailwind to work

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "CandidateValidate - Know Your Leader",
  description: "Verify your politician's criminal records and assets.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}