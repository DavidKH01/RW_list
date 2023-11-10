






let listTest = "this is a test"
document.getElementById('show_list').innerHTML = listTest;

if (true){
    console.log("scripts in html");
};

//need async funciton to fetch data from url
//
async function test () {
    try {
        let fetch_data = await fetch('http://127.0.0.1:5000');
        let data = await fetch_data.json();
        //Have to turn stingigy data because its a dictionary/Object??
        let jsonString = JSON.stringify(data);
        console.log(typeof jsonString);
        document.getElementById('show_list').innerHTML=`${jsonString}`
    } catch (error) {
        console.error('Error:', error);
    }
}

async function getNames() {
    try {
        // Fetch data from flask app route URL
        let response = await fetch('http://127.0.0.1:5000/getNames');
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        let data = await response.json();
        // document.getElementById('show_test').innerHTML=`${data}`;

        let tl = document.getElementById('tile1');
        let ul = document.createElement('ul');

        for (let i = 0; i < data.length; ++i) {
            let li = document.createElement('li');
            li.innerHTML = data[i];
            ul.appendChild(li);
        }

        tl.appendChild(ul);
    } catch (error) {
        console.error('Error:', error);
    }
}

//test()
getNames()

