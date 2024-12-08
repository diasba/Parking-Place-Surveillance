import Grid from '@mui/material/Grid2';
import { Header } from './components/Header';
import { ParkingSpot } from './components/ParkingSpot';
import { useEffect, useState } from 'react';
import { Container } from '@mui/material';

type ParkingSpot = {
  id: number;
  occupied: boolean;
  prediction: number;
};

function App() {
  const [parkingSpots, setParkingSpots] = useState<ParkingSpot[]>([]);
  const fetchData = async () => {
    try {
      const response = await fetch('/mockData.json');
      console.log(response);
      const body = (await response.json()) as ParkingSpot[];
      setParkingSpots(body);
    } catch (error) {
      console.error('Error: ', error);
    }
  };

  useEffect(() => {
    void fetchData();
  }, []);

  console.log(parkingSpots);

  return (
    <>
      <Header />
      <main>
        <Container>
          <Grid
            display='flex'
            justifyContent='center'
            alignItems='center'
            data-testid='parking-grid'
            container
            spacing={2}
          >
            {parkingSpots.map((parkingSpot) => (
              <ParkingSpot
                key={parkingSpot.id}
                title={'Parking Spot ' + parkingSpot.id}
                occupied={parkingSpot.occupied}
                prediction={parkingSpot.prediction}
              />
            ))}
          </Grid>
        </Container>
      </main>
    </>
  );
}

export default App;
