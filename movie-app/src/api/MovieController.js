const MoviesController = (container) => ({
	createMovie: async (req, res) => {
		const { CreateMovieUseCase } = container
		const { title, synopsis, duration } = req.body

		const movie = await CreateMovieUseCase(title, synopsis, duration)
		res.code(201).send(movie)
	}
})

export default MoviesController
