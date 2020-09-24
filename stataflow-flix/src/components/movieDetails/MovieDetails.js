import React, { useState, useEffect } from "react";

export default function MovieDetails(props) {
  const { match } = props;

  console.log(match);

  return (
    <div>
      <h1>{match.params.movieID}</h1>
    </div>
  );
}
