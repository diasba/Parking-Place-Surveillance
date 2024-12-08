import Grid from '@mui/material/Grid2';
import { Header } from './components/Header';
import { ParkingSpot } from './components/ParkingSpot';
import { useEffect, useState } from 'react';
import { Container } from '@mui/material';

type ParkingSpot = {
  spot_id: number;
  status: string;
  prediction: number | null;
};

function App() {
  const [parkingSpots, setParkingSpots] = useState<ParkingSpot[]>([]);
  const fetchData = async () => {
    try {
      const response = await fetch('/api/parking_status'); //Using proxy
      const body = (await response.json()) as ParkingSpot[];
      console.log("Fetched Parking Spots:", body);  // Log data in frontend console
      setParkingSpots(body);
    } catch (error) {
      console.error('Error: ', error);
    }
  };

  useEffect(() => {
    void fetchData();
  }, []);

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
                key={parkingSpot.spot_id}
                title={'Parking Spot ' + parkingSpot.spot_id}
                occupied={parkingSpot.status === 'OCCUPIED'}
                prediction={parkingSpot.prediction !== null ? parkingSpot.prediction.toString() : ''}
              />
            ))}
          </Grid>
        </Container>
      </main>
    </>
  );
}

export default App;