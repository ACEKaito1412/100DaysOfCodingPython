// Function to fetch data from JSON file
async function loadData() {
    try {
        const response = await fetch("static/js/data.json"); // Load the JSON file
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json(); // Parse JSON

        displayWork(data.work);
        displayStudies(data.studies);
    } catch (error) {
        console.error("Error fetching JSON:", error);
    }
}

// Function to display work experience
function displayWork(workData) {
    const workList = document.getElementById("work-container");
    workList.innerHTML = ""; // Clear existing content

    workData.forEach(job => {
        const div_main = document.createElement("div");
        const div_sec = document.createElement("div");
        const div_third = document.createElement("div");
        const title = document.createElement("h6");
        const company = document.createElement("p");
        const date = document.createElement("p");
        const skill = document.createElement('p');

        div_main.classList.add("d-flex", "gap-3", "py-3", "border-0", "bg-transparent");
        div_sec.classList.add("d-flex", "gap-2", "w-100" ,"justify-content-start" ,"align-items-center");


        title.classList.add("mb-0","text-uppercase");
        company.classList.add("mb-0", "opacity-75", "text-secondary");
        date.classList.add("mb-0", "opacity-75", "text-secondary");
        skill.classList.add("mb-0", "secondary-text", "fw-bold" ,"opacity-75")
        
        title.innerHTML = `${job.position}`;
        company.innerHTML = `${job.company}`;
        date.innerHTML = `${job.start_date} - ${job.end_date}`;

        const skill_list = job.skills;
        skill_list.forEach((name) => {
            const span = document.createElement("span");
            span.classList.add("me-2");
            span.innerHTML = name;

            skill.appendChild(span)
        })

        div_third.appendChild(title);
        div_third.appendChild(company);
        div_third.appendChild(skill);
        div_third.appendChild(date);

        div_sec.appendChild(div_third);
        div_main.appendChild(div_sec);
        workList.appendChild(div_main);
    });
}

// Function to display studies
function displayStudies(workData) {
    const workList = document.getElementById("cert-container");
    workList.innerHTML = ""; // Clear existing content

    workData.forEach(job => {
        const div_main = document.createElement("div");
        const div_sec = document.createElement("div");
        const div_third = document.createElement("div");
        const field = document.createElement("h6");
        const institution = document.createElement("p");
        const topic = document.createElement('div');
        

        div_main.classList.add("d-flex", "gap-3", "py-3", "border-0", "bg-transparent");
        div_sec.classList.add("d-flex", "gap-2", "w-100" ,"justify-content-start" ,"align-items-center");


        field.classList.add("mb-0","text-uppercase");
        institution.classList.add("mb-0", "opacity-75", "text-secondary");
        topic.classList.add("mb-0", "secondary-text", "fw-bold" ,"opacity-75", "d-flex", "flex-wrap");
        
        field.innerHTML = `${job.field}`;
        institution.innerHTML = `${job.institution}`;

        var button;
        if(job.link == ""){
            button =  document.createElement('button');
            button.classList.add("btn","btn-sm", "btn-outline-secondary", "no-hover" ,"mt-2");
            button.dissabled = true;
            button.innerHTML = "View Certificate";
            button.target = "_blank";
            button.style.cursor = "not-allowed";
            button.style.opacity = "0.5";
        }else{
            button =  document.createElement('a');
            button.classList.add("btn","btn-outline-secondary","btn-sm","mt-2");
            button.innerHTML = "View Certificate";
            button.target = "_blank";
            button.href = `${job.link}`;
        }
       



        const topic_list = job.topics;
        topic_list.forEach((name) => {
            const span = document.createElement("span");
            span.classList.add("me-2");

            span.innerHTML = name;

            topic.appendChild(span)
        })

        div_third.appendChild(field);
        div_third.appendChild(institution);
        div_third.appendChild(topic);
        div_third.appendChild(button);


        div_sec.appendChild(div_third);
        div_main.appendChild(div_sec);
        workList.appendChild(div_main);
    });
}

// Load JSON data on page load
loadData();