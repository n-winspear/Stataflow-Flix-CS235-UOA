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
import axios from "axios";

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

export default function MediaCard(props) {
  const classes = useStyles();
  const { movieData, apiURL } = props;
  const [ratingState, setRatingState] = useState(false);

  function changeRatingState() {
    setRatingState(!ratingState);
  }

  async function postRating(rating) {
    let config = {
      method: "post",
      url: `${apiURL}/reviews`,
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
        "Access-Control-Allow-Origin": "*",
      },
      data: {
        movie: movieData.title,
        rating: rating,
        reviewText: "",
      },
    };
    let res = await axios(config);
    console.log(res);
    changeRatingState();
  }

  return (
    <Card className={classes.root}>
      <CardActionArea onClick={() => props.viewMovie(movieData)}>
        <CardMedia
          className={classes.media}
          title={movieData.title}
          image={TempMovieImage}
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="h2">
            {movieData.title.length > 26
              ? `${movieData.title.slice(0, 21)}...`
              : movieData.title}
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
            <RatingStars postRating={postRating} />
          </Box>
        ) : (
          <Button size="small" color="primary" onClick={changeRatingState}>
            Rate
          </Button>
        )}
      </CardActions>
    </Card>
  );
}
