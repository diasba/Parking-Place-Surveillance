import AppBar from '@mui/material/AppBar';
import Typography from '@mui/material/Typography';

export const Header = () => {
  return (
    <header>
      <AppBar sx={{ padding: '0.5rem 1rem' }}>
        <Typography variant='h6' sx={{ flexGrow: 1 }}>
          Free Parking
        </Typography>
      </AppBar>
    </header>
  );
};
