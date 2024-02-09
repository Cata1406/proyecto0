import * as React from "react";
import IconButton from "@mui/material/IconButton";
import Menu from "@mui/material/Menu";
import MenuItem from "@mui/material/MenuItem";
import MoreVertIcon from "@mui/icons-material/MoreVert";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";

const options = ["None", "Atria"];

const ITEM_HEIGHT = 48;

interface ThreeDotsProps {
    setOpenPopUpEditTask: React.Dispatch<React.SetStateAction<boolean>>;
    setIsTaskUpdate: React.Dispatch<React.SetStateAction<boolean>>;
}

export default function ThreeDots({
    setOpenPopUpEditTask,
    setIsTaskUpdate,
}: ThreeDotsProps) {
    const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);
    const open = Boolean(anchorEl);

    const handleClick = (event: React.MouseEvent<HTMLElement>) => {
        setAnchorEl(event.currentTarget);
    };

    const handleClickEditTask = () => {
        setOpenPopUpEditTask(true);
        setAnchorEl(null);
        setIsTaskUpdate(true);
    };

    const handleClose = () => {
        setAnchorEl(null);
    };

    return (
        <div>
            <IconButton
                aria-label="more"
                id="long-button"
                aria-controls={open ? "long-menu" : undefined}
                aria-expanded={open ? "true" : undefined}
                aria-haspopup="true"
                onClick={handleClick}
            >
                <MoreVertIcon />
            </IconButton>
            <Menu
                id="long-menu"
                MenuListProps={{
                    "aria-labelledby": "long-button",
                }}
                anchorEl={anchorEl}
                open={open}
                onClose={handleClose}
            >
                <MenuItem onClick={handleClickEditTask}>
                    <EditIcon />
                    {"Edit task"}
                </MenuItem>
                <MenuItem onClick={handleClose}>
                    <IconButton aria-label="delete">
                        <DeleteIcon />
                    </IconButton>
                    {"Delete task"}
                </MenuItem>
            </Menu>
        </div>
    );
}
