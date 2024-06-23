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
        white: "#fff",
        black: "#000",
        darkgray: "#9f9f9f",
        gainsboro: "#e6e6e6",
        gray: {
          "100": "#8a8a8a",
          "200": "rgba(0, 0, 0, 0.3)",
        },
        saddlebrown: "#6f442a",
        crimson: "#d91b20",
        coral: "#e56946",
        deeppink: "#db0f74",
        darkslateblue: "#2f58ab",
        orange: "#e7911f",
        forestgreen: "#0c8e3c",
        khaki: "#e0cb6f",
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