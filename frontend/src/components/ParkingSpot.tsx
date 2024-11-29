import { Typography } from "@mui/material";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import { green, red } from "@mui/material/colors";
import React, { useState } from "react";

type ParkingSpotProps = {
  title: string;
  occupied: boolean;
  prediction: number;
};

export const ParkingSpot = ({
  title,
  occupied,
  prediction,
}: ParkingSpotProps) => {
  return (
    <Card
      sx={{ minWidth: 275, backgroundColor: occupied ? red[400] : green[400] }}
    >
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
