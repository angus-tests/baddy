/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flyonui/dist/js/*.js',
  ],
  theme: {
    extend: {
      colors: {
        sand: {
          DEFAULT: "#F9F5E1",  // Light mode color
          dark: "#1A1821",     // Dark mode variant
      },
      },
    },
  },
  flyonui: {

    themes: [
      {
        light: {
          ...require("flyonui/src/theming/themes")["light"],
          "primary": "#F43F5E",
          "primary-content": "#FFFFFF",

        }
      },
      {
        dark: {
          ...require("flyonui/src/theming/themes")["dark"],
          "primary": "#F43F5E",
          "primary-content": "#FFFFFF",
        }
      },
    ]

  },
  darkMode: ['class', '[data-theme="dark"]'],
  plugins: [
    require('@tailwindcss/typography'),
    require('flyonui'),
    require('flyonui/plugin')
  ],

}

