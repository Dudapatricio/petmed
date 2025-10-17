/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // Django templates
    "./templates/**/*.html",
    "./**/templates/**/*.html",
    
    // Static files
    "./static/**/*.js",
    
    // Apps do Django
    "./**/apps.py",
    "./**/views.py",
    
    // HTML, JS, etc.
    "./*.html",
    "./**/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
  daisyui: {
    themes: ["light", "dark", "cupcake"],
  },
}