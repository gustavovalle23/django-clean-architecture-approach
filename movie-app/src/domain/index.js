import buildMakeMovie from './movie.js'

const Id = { makeId: () => '123' }
const validator = (args) => {
	return { errors: [] }
}

const makeMovie = buildMakeMovie({ Id, validator })

const movie = makeMovie({ title: 'Title', synopsis: 'A few detail', duration: 120 })

export default makeMovie
