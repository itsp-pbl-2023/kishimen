module.exports = {
  root: true,
  parserOptions: {
    parser: '@typescript-eslint/parser'
  },
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/eslint-recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:vue/vue3-recommended',
    'prettier'
  ],
  plugins: ['unused-imports'],
  rules: {
    'no-console': 'warn',
    'no-debugger': 'warn',
    'no-empty': ['error', { allowEmptyCatch: true }],
    eqeqeq: 'error',
    'vue/eqeqeq': 'error',
    '@typescript-eslint/explicit-module-boundary-types': 'off',
    '@typescript-eslint/member-delimiter-style': [
      'error',
      {
        multiline: {
          delimiter: 'none'
        },
        singleline: {
          delimiter: 'semi'
        }
      }
    ],
    '@typescript-eslint/consistent-type-imports': 'error',
    '@typescript-eslint/no-unused-vars': 'off',
    'unused-imports/no-unused-imports': 'warn',
    'unused-imports/no-unused-vars': 'off',
    'vue/require-default-prop': 'off',
    'vue/no-v-html': 'off',
    'vue/block-lang': [
      'error',
      {
        script: { lang: 'ts' },
        style: { lang: 'scss' }
      }
    ],
    'vue/component-api-style': ['error', ['script-setup']],
    'vue/component-name-in-template-casing': ['error', 'kebab-case'],
    'vue/v-on-event-hyphenation': ['error', 'always', { autofix: true }],
    'vue/v-on-function-call': 'error',
    'vue/no-template-target-blank': 'error',
    'vue/prefer-true-attribute-shorthand': 'error'
  },
  overrides: [
    {
      // 直下のファイル
      files: ['*.cjs'],
      excludedFiles: ['*/**/*.cjs'],
      env: {
        node: true
      },
      rules: {
        '@typescript-eslint/no-var-requires': 'off'
      }
    }
  ],
  reportUnusedDisableDirectives: true
}
