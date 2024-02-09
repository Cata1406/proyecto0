import { Box, List, ListItem } from "@mui/material";
import Task from "./Task";

interface TaskListProps {
    setOpenPopUpEditTask: React.Dispatch<React.SetStateAction<boolean>>;
    setIsTaskUpdate: React.Dispatch<React.SetStateAction<boolean>>;
}

const TaskList = ({ setOpenPopUpEditTask, setIsTaskUpdate }: TaskListProps) => {
    return (
        <Box>
            <List>
                {[1, 2, 3].map((task) => (
                    <ListItem key={task}>
                        <Task
                            setOpenPopUpEditTask={setOpenPopUpEditTask}
                            setIsTaskUpdate={setIsTaskUpdate}
                        />
                    </ListItem>
                ))}
            </List>
        </Box>
    );
};

export default TaskList;
