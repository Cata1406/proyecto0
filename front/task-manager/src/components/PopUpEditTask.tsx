//import { AccountCircle } from "@mui/icons-material";
import dayjs, { Dayjs } from "dayjs";
import {
    Button,
    Dialog,
    DialogContent,
    Divider,
    FormControl,
    InputLabel,
    MenuItem,
    Select,
    SelectChangeEvent,
    Stack,
    TextField,
} from "@mui/material";
import React from "react";
//import Task from "./Task";
import { TimePicker } from "@mui/x-date-pickers/TimePicker";
import { DatePicker } from "@mui/x-date-pickers/DatePicker";
import { LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";

interface PopUpEditTaskProps {
    openPopUpEditTask: boolean;
    setOpenPopUpEditTask: React.Dispatch<React.SetStateAction<boolean>>;
    handleClose: () => void;
    isUpdate: boolean;
    setIsTaskUpdate: React.Dispatch<React.SetStateAction<boolean>>;
}

const PopUpEditTask = ({
    openPopUpEditTask,
    setOpenPopUpEditTask,
    handleClose,
    isUpdate,
    setIsTaskUpdate,
}: PopUpEditTaskProps) => {
    const handleClick = () => {
        setOpenPopUpEditTask(false);
    };

    return (
        <Dialog
            open={openPopUpEditTask}
            onClose={handleClose}
            aria-labelledby="alert-dialog-title"
            aria-describedby="alert-dialog-description"
        >
            <DialogContent>
                <Stack spacing={2} direction="column">
                    <TextField
                        id="input-with-sx"
                        label="Task description"
                        variant="standard"
                    />
                    <TaskButtons />
                    <Divider />
                    <Stack
                        spacing={2}
                        direction="row"
                        justifyContent="space-between"
                    >
                        <Button
                            variant="contained"
                            size="medium"
                            onClick={handleClose}
                        >
                            {"Cancel"}
                        </Button>
                        <Button
                            variant="contained"
                            size="medium"
                            onClick={handleClick}
                        >
                            {isUpdate ? "Update task" : "Add task"}
                        </Button>
                    </Stack>
                </Stack>
            </DialogContent>
            {/* <DialogActions> */}
            {/* <Button onClick={handleClose}>Disagree</Button> */}
            {/* <Button onClick={handleClose} autoFocus> */}
            {/* Agree */}
            {/* </Button> */}
            {/* </DialogActions> */}
        </Dialog>
    );
};

const TaskButtons = () => {
    const [date, setDate] = React.useState<Dayjs | null>(dayjs("2022-04-17"));
    const [time, setTime] = React.useState<Dayjs | null>(
        dayjs("2022-04-17T15:30")
    );

    const handleDatePickerChange = (newDate: Dayjs | null) => {
        setDate(newDate);
    };

    const handleTimePickerChange = (newTime: Dayjs | null) => {
        setTime(newTime);
    };

    const [category, setCategory] = React.useState("");
    const [status, setStatus] = React.useState("");

    const handleChangeEditCategory = (event: SelectChangeEvent) => {
        setCategory(event.target.value as string);
    };
    const handleChangeEditStatus = (event: SelectChangeEvent) => {
        setStatus(event.target.value as string);
    };

    return (
        <Stack spacing={2} direction="column">
            <LocalizationProvider dateAdapter={AdapterDayjs}>
                <DatePicker
                    label="Date"
                    value={date}
                    onChange={handleDatePickerChange}
                />
                <TimePicker
                    label="Time"
                    value={time}
                    onChange={handleTimePickerChange}
                />
            </LocalizationProvider>
            <FormControl fullWidth>
                <InputLabel id="demo-simple-select-label">Category</InputLabel>
                <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={category}
                    label="Category"
                    onChange={handleChangeEditCategory}
                >
                    <MenuItem value={"Work"}>Work</MenuItem>
                    <MenuItem value={"University"}>University</MenuItem>
                    <MenuItem value={"House chores"}>House chores</MenuItem>
                </Select>
            </FormControl>
            <FormControl fullWidth>
                <InputLabel id="demo-simple-select-label">Status</InputLabel>
                <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={status}
                    label="Status"
                    onChange={handleChangeEditStatus}
                >
                    <MenuItem value={"TODO"}>Todo</MenuItem>
                    <MenuItem value={"IN_PROGRESS"}>In progress</MenuItem>
                    <MenuItem value={"DONE"}>Done</MenuItem>
                </Select>
            </FormControl>
        </Stack>
    );
};

export default PopUpEditTask;
