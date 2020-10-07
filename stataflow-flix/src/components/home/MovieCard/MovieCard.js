import React, { useState } from "react";
import { Box } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import TempMovieImage from "components/home/images/TempMovieImage.jpg";
import TextTruncate from "react-text-truncate";
import RatingStars from "components/home/MovieCard/RatingStars";

const useStyles = makeStyles({
  root: {
    width: 352,
  },
  media: {
    height: 198,
    flexGrow: 1,
  },
  ratingBox: {
    paddingLeft: "0.5em",
  },
});

export default function MovieCard(props) {
  const classes = useStyles();
  const { movieData, apiURL, viewMovie, userID } = props;
  const [ratingState, setRatingState] = useState(false);

  return (
    <Card className={classes.root}>
      <CardActionArea onClick={() => viewMovie(movieData)}>
        <CardMedia
          className={classes.media}
          title={movieData.movieTitle}
          image={TempMovieImage}
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="h2">
            {movieData.movieTitle.length > 26
              ? `${movieData.movieTitle.slice(0, 21)}...`
              : movieData.movieTitle}
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p">
            <TextTruncate
              line={2}
              element="span"
              truncateText="…"
              text={movieData.description}
            />
          </Typography>
        </CardContent>
      </CardActionArea>
      <CardActions>
        {ratingState ? (
          <Box className={classes.ratingBox}>
            <RatingStars
              movieTitle={movieData.title}
              apiURL={apiURL}
              userID={userID}
            />
          </Box>
        ) : (
          <Button
            size="small"
            color="primary"
            onClick={() => setRatingState(!ratingState)}
          >
            Rate
          </Button>
        )}
      </CardActions>
    </Card>
  );
}
