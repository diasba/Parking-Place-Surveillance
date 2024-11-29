import React from "react";
import AppBar from '@mui/material/AppBar';
import Typography from "@mui/material/Typography";

export const Header = () => {
  return (
    <AppBar>
      <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
        The App
      </Typography>{" "}
    </AppBar>
  );
};
