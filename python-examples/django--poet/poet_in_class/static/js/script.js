function formEventHandler(event) {
    event.preventDefault();

    let form = event.target;
    let url = form.action;

    let request = {
        method: form.method,
        body: form,
        mode: "same-origin",
        headers: {
            "x-csrftoken": form.elements["csrfmiddlewaretoken"].value,
        },
    }

    fetch(url, request)
    .then(resp => console.log(resp))
}

function sendFavorite(source, url) {
    fetch(url)
    .then(resp => resp.json())
    .then(json => {
        if (json.message === "Your favorite was added :)") {
            source.textContent = `${json.numLikes} favorites`;
        }

        alert(json.message);
    })
}
