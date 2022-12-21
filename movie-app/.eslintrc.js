module.exports = {
	parser: '@typescript-eslint/parser',
	parserOptions: {
	  project: 'tsconfig.json',
	  tsconfigRootDir : __dirname,
	  sourceType: 'module',
	},
	plugins: ['@typescript-eslint/eslint-plugin', 'import-helpers', 'unused-imports'],
	extends: [
	  'plugin:@typescript-eslint/recommended',
	  'plugin:prettier/recommended',
	],
	root: true,
	env: {
	  node: true,
	  jest: true,
	},
	ignorePatterns: ['.eslintrc.js'],
	rules: {
	  '@typescript-eslint/interface-name-prefix': 'off',
	  '@typescript-eslint/explicit-function-return-type': 'off',
	  '@typescript-eslint/explicit-module-boundary-types': 'off',
	  '@typescript-eslint/no-explicit-any': 'off',
	  '@typescript-eslint/no-namespace': 'off',
	  'import-helpers/order-imports': [
		'warn',
		{
		  'newlinesBetween': 'always',
		  'groups': [
			['module', 'absolute'],
			'/^@\//',
			['parent', 'sibling', 'index']
		  ],
		  'alphabetize': { 'order': 'asc', 'ignoreCase': true }
		}
	  ],
	  "no-unused-vars": "off",
	  "unused-imports/no-unused-imports": "error",
	  "unused-imports/no-unused-vars": [
		"warn",
		{
		  "vars": "all",
		  "varsIgnorePattern": "^_",
		  "args": "after-used",
		  "argsIgnorePattern": "^_"
		}
	  ]
	},
  };
