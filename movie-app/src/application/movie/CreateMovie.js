const CreateMovieUseCase = ({ MovieRepository, Movie }) =>
	(title, synopsis, duration) => {
		const movie = new Movie({ title, synopsis, duration })
		return MovieRepository.save(movie)
	}

export default CreateMovieUseCase;
