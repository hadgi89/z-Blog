module.exports = {
    settings: {
      "vetur.useWorkspaceDependencies": true,
      "vetur.experimental.templateInterpolationService": true
    },
    projects: [
      './nuxt', 
      {
        root: './nuxt',
        package: './package.json',
        tsconfig: './tsconfig.json',
        snippetFolder: './.vscode/vetur/snippets',
        globalComponents: [
          './src/components/**/*.vue'
        ]
      }
    ]
  }