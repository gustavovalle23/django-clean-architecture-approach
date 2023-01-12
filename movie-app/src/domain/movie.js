const buildMakeMovie = ({ Id, validator }) => ({
	id = Id.makeId(),
	title,
	synopsis,
	duration,
} = {}) => {
	const { error } = validator({
		id, title, synopsis, duration,
	});
	if (error) throw new Error(error);

	return Object.freeze({
		getId: () => id,
		getTitle: () => title,
		getSynopsis: () => synopsis,
		getDuration: () => duration,
	});
};


export default buildMakeMovie
