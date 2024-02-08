import React from 'react';
import { Box, Typography } from '@mui/material';
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import { COLORS } from "../styles/colors";

const Header = () => {


  return (
      <Box className="header">
        <AppBar position="static" sx={{ backgroundColor: "white" }}>
            <Toolbar className="first-row">
                <LogoTaskManager taskManagerText="TaskManager" />

            </Toolbar>
        </AppBar>
        </Box>
  );
}

export default Header;

const LogoTaskManager = ({
    taskManagerText,
    //navigate,
  }: {
    taskManagerText: string;
    //navigate: NavigateFunction;
  }) => (
    <Toolbar>
      <Typography
        variant="h5"
        style={{ color: COLORS.primary, fontWeight: "bold" }}
        //onClick={() => navigate("/")}
      >
        {taskManagerText}
      </Typography>
    </Toolbar>
  );
  