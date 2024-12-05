import { Chip, Divider, Typography, useMediaQuery } from '@mui/material';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import { green, red } from '@mui/material/colors';

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
  const desktopView = useMediaQuery('(min-width:600px)');
  return (
    <Card
      data-testid='parking-spot-card'
      sx={
        desktopView
          ? {
              minWidth: '12rem',
              minHeight: '12rem',
              backgroundColor: occupied ? red[400] : green[400],
            }
          : {
              minWidth: '12rem',
              minHeight: '10rem',
              backgroundColor: occupied ? red[400] : green[400],
            }
      }
    >
      <CardContent sx={{ height: '100%' }}>
        <Typography
          gutterBottom
          variant={desktopView ? 'h5' : 'h6'}
          sx={desktopView ? { marginBottom: '3rem' } : { marginBottom: '1rem' }}
        >
          {title}
        </Typography>
        {occupied ? (
          <Chip label='Occupied' color='error' sx={{ marginY: '0.25rem' }} />
        ) : (
          <Chip label='Free' color='success' sx={{ marginY: '0.25rem' }} />
        )}
        <Divider />
        {occupied ? (
          <Typography sx={{ marginY: '0.25rem' }}>
            Available in: {prediction}
          </Typography>
        ) : null}
      </CardContent>
    </Card>
  );
};
