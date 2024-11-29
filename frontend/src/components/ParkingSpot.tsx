import { Typography } from "@mui/material";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import { green } from "@mui/material/colors";
import React, { useState } from "react";

type ParkingSpotProps = {
    title: string;
}

export const ParkingSpot = ({title}: ParkingSpotProps) => {
  const [occupied, setOccupied] = useState(false);
  const [prediction, setPrediction] = useState(0);

  return (
    <Card sx={{ minWidth: 275, backgroundColor: green[400] }}>
      <CardContent>
        <Typography variant="h5">{title}</Typography>
        <br />
        {occupied ? "Occupied" : "Free"}
        <br />
        Free in: {prediction}
      </CardContent>
    </Card>
  );
};
