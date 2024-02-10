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
import { TaskDetails } from "./TaskList";

interface TaskProps {
    setOpenPopUpEditTask: React.Dispatch<React.SetStateAction<boolean>>;
    setIsTaskUpdate: React.Dispatch<React.SetStateAction<boolean>>;
    task_details: TaskDetails;
}

const Task = ({
    setOpenPopUpEditTask,
    setIsTaskUpdate,
    task_details,
}: TaskProps) => {
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
                            {task_details.text}
                        </Typography>
                        <TaskButtons
                            setOpenPopUpEditTask={setOpenPopUpEditTask}
                            setIsTaskUpdate={setIsTaskUpdate}
                            task_details={task_details}
                        />
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

const TaskButtons = ({
    setOpenPopUpEditTask,
    setIsTaskUpdate,
    task_details,
}: TaskProps) => (
    <Stack spacing={2} direction="row">
        {[task_details.forseen_end_date, "Category", task_details.state].map(
            (text) => (
                <Chip key={text} label={text} />
            )
        )}
    </Stack>
);

export default Task;
