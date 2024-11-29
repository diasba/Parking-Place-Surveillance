import Grid from "@mui/material/Grid2";
import { Header } from "./components/Header";
import { ParkingSpot } from "./components/ParkingSpot";
import { useEffect, useState } from "react";

type ParkingSpot = {
  id: number;
  occupied: boolean;
  prediction: number;
};

function App() {
  const [parkingSpots, setParkingSpots] = useState<ParkingSpot[]>([]);

  const fetchData = async () => {
    try {
      const response = await fetch("/mockData.json");
      const body = await response.json() as ParkingSpot[];
      setParkingSpots(body);
    } catch (error) {
      console.error("Error fetching data: ", error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <>
      <Header />
      <Grid container spacing={2}>
        <ParkingSpot title="Parking Spot 1" />
        <ParkingSpot title="Parking Spot 2" />
        <ParkingSpot title="Parking Spot 3" />
        <ParkingSpot title="Parking Spot 4" />
        <ParkingSpot title="Parking Spot 5" />
      </Grid>
    </>
  );
  /*
    {
      id:
    }
  */
}

export default App;
