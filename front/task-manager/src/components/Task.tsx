import {
    Box,
    Card,
    CardContent,
    Checkbox,
    Chip,
    IconButton,
    Stack,
    Typography,
} from "@mui/material";
import ThreeDots from "./ThreeDots";

interface TaskProps {
    setOpenPopUpEditTask: React.Dispatch<React.SetStateAction<boolean>>;
    setIsTaskUpdate: React.Dispatch<React.SetStateAction<boolean>>;
}

const Task = ({ setOpenPopUpEditTask, setIsTaskUpdate }: TaskProps) => {
    return (
        <div className="task">
            <Card sx={{ display: "flex" }}>
                <Box>
                    <Checkbox />
                </Box>
                <Box sx={{ display: "flex", flexDirection: "column" }}>
                    <CardContent sx={{ flex: "1 0 auto" }}>
                        <Typography
                            component="div"
                            variant="h5"
                            sx={{ flexGrow: 1 }}
                        >
                            Texto tarea
                        </Typography>
                        <TaskButtons />
                    </CardContent>
                </Box>
                <ThreeDots
                    setOpenPopUpEditTask={setOpenPopUpEditTask}
                    setIsTaskUpdate={setIsTaskUpdate}
                />
            </Card>
        </div>
    );
};

const TaskButtons = () => (
    <Stack spacing={2} direction="row">
        {["Date", "Category", "Status"].map((text) => (
            <Chip key={text} label={text} />
        ))}
    </Stack>
);

export default Task;
