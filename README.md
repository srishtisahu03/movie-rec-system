# movie-recommendation-system

This repository contains a content-based movie recommendation system that suggests similar movies based on user preferences. The system analyzes movie attributes such as genres, keywords, cast, and crew to identify patterns and recommend movies with similar characteristics.

## Project Overview

The recommendation system uses natural language processing techniques to process textual data about movies and find similarities between them. When a user selects a movie they like, the system identifies and recommends movies with similar content features.

## Features

- Content-based movie recommendation
- Text processing and feature extraction from movie metadata
- Similarity score calculation using cosine similarity
- Interactive movie selection and recommendation

## Dataset

The project uses the TMDB 5000 Movie Dataset, which includes:  
- Movie metadata (title, genres, overview, etc.)
- Cast and crew information
- User ratings
- Production details

## How It Works

1. The system processes movie metadata including plot summaries, keywords, cast, and crew
2. Text processing techniques are applied to extract relevant features
3. A similarity matrix is created using cosine similarity
4. When a user selects a movie, the system finds movies with the highest similarity scores
5. The top N most similar movies are recommended to the user

## Future Improvements

- Add collaborative filtering for hybrid recommendations
- Implement a web interface for easier interaction
- Include more recent movies with updated datasets
- Enhance recommendation accuracy with advanced NLP techniques
- Add user profiles to personalize recommendations over time

## Contributing

Contributions to improve the prediction model or add more analysis dimensions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is open-source and free to use.

## Contact

Srishti Sahu - srishtisahu2006@gmail.com  
Project Link: https://github.com/srishtisahu03/moviee-rec-system
