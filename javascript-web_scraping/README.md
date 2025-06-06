
#!/bin/bash

# Prompt user for their name
echo -n "Enter your name: "
read user_name

# Set up the base directory with the user's name
base_dir="submission_reminder_${user_name}"
# create the main directory
mkdir -p "$base_dir/{app,config,modules,assets}"

touch "$base_dir/config/config.env"
touch "$base_dir/app/reminder.sh && chmod u+x base_dir/app/reminder.sh"
touch "$base_dir/modules/functions.sh && chmod u+x base_dir/modules/functions.sh"
touch "$base_dir/startup.sh && chmod u+x base_dir/startup.sh"
touch "$base_dir/assets/submissions.txt"
echo 'student, assignment, submission status
here, Shell Navigation, submitted
Aaliyah, Shell Navigation, not submitted
Ange, Shell Navigation, not submitted
kean, Shell Navigation, not submitted
kezia, Shell Navigation, submitted
rein, Shell Navigation, not submitted
rinnah, Shell Navigation, submitted' > "$base_dir/assets/submissions.txt"
echo '# This is the config file
ASSIGNMENT="Shell Navigation"
DAYS_REMAINING=2' > "$base_dir/config/config.env"
echo '#!/bin/bash

# Function to read submissions file and output students who have not submitted
function check_submissions {
    local submissions_file=$1
    echo "Checking submissions in $submissions_file"

    # Skip the header and iterate through the lines
    while IFS=, read -r student assignment status; do
        # Remove leading and trailing whitespace
        student=$(echo "$student" | xargs)
        assignment=$(echo "$assignment" | xargs)
        status=$(echo "$status" | xargs)
	# Check if assignment matches and status is 'not submitted'
        if [[ "$assignment" == "$ASSIGNMENT" && "$status" == "not submitted" ]]; then
            echo "Reminder: $student has not submitted the $ASSIGNMENT assignment!"
        fi
    done < <(tail -n +2 "$submissions_file") # Skip the header
}' > "$base_dir/modules/functions.sh"
echo '#!/bin/bash

# Source environment variables and helper functions
source ./config/config.env
