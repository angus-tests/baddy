/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flyonui/dist/js/*.js',
  ],
  theme: {
    extend: {},
  },
  flyonui: {

    themes: [
      {
        light: {
          ...require("flyonui/src/theming/themes")["light"],
          "primary": "#F43F5E",
          "primary-content": "#FFFFFF",
          "base-100": "#F9F5E1",
          "base-200": "#EBE8D8",
          "base-300": "#CAC8BA",
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

