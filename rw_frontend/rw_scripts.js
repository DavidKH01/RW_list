
let listTest = "this is a test"
document.getElementById('show_list').innerHTML = listTest;

if (true){
    console.log("scripts in html");
};

function test () {
    let fetch_data = fetch('http://127.0.0.1:5000')
        // res is the data or (response) from the fetch
        //.json() method. This method reads the response body as JSON and returns a Promise that resolves to the parsed JavaScript object or data structure.
        .then(res => res.json())
        
        .then(res => JSON.stringify(res))
        
        .then(res => {console.log(res); document.getElementById('show_list').innerHTML=`${res}` })
    
        //  this code works but missing the name of the variable in the ${} that will print the data
        // .then(res => res.json())
        // .then(res => console.log(res))
        // .then(res =>{show_test.innerHTML=`this should be list: ${}`})

        //This will overwrite anyone in the show_list id once run
        document.getElementById('show_list').innerHTML= "This is where the list goes"
        
        
}

// test()

