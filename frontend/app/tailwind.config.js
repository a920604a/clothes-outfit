/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ["class"],
  content: [
    './pages/**/*.{ts,tsx}',
    './components/**/*.{ts,tsx}',
    './app/**/*.{ts,tsx}',
    './src/**/*.{ts,tsx}',
  ],
  prefix: "",
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      keyframes: {
        "accordion-down": {
          from: { height: "0" },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: "0" },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      },
      colors: {
        black: "#000",
        white: "#fff",
        gray: {
          100: "#8a8a8a",
          50: "#8a8a8a80"
        },
        silver: "#c0c0c0",
        darkslateblue: "#2f58ab",
        crimson: "#d91b20",
        saddlebrown: "#6f442a",
        khaki: "#e0cb6f",
        forestgreen: "#0c8e3c",
        orange: "#e7911f"
      },
      spacing: {
        "spacing-m": "48px",
      },
      fontFamily: {
        "arimo-hebrew-subset-italic": "'Arimo Hebrew Subset Italic'",
        damion: "Damion",
        "body-text": "Inter",
        kreon: "Kreon",
        "noto-sans-cjk-tc": "'Noto Sans CJK TC'",
      },
    },
    fontSize: {
      xl: "20px",
      base: "16px",
      "21xl": "40px",
      "13xl": "32px",
      "5xl": "24px",
      lgi: "19px",
      inherit: "inherit",
    },
    screens: {
      mq825: {
        raw: "screen and (max-width: 825px)",
      },
      mq675: {
        raw: "screen and (max-width: 675px)",
      },
      mq450: {
        raw: "screen and (max-width: 450px)",
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
}