/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flyonui/dist/js/*.js',
  ],
  theme: {
    extend: {
      colors: {
        "sand": "#F9F5E1",
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
    ]

    },
  plugins: [
    require('@tailwindcss/typography'),
    require('flyonui'),
    require('flyonui/plugin')
  ],

}

