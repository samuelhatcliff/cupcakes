const BASE_URL = "http://127.0.0.1:5000"



function populate(data) {
    for (let cupcake of data) {
        const newCup = makeCupcake(cupcake);
        $("#cupcakes-list").append(newCup);
    }
}

function makeCupcake(cupcake) {
    let newCup = `<div data-cupcake-id=${cupcake.id}>
            <l1>${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
            <button class="delete-cupcake">X</button>
            </l1>
            <img class= "cupcake-img" src=${cupcake.photo_url}>
            </div>`;
    return newCup;
}

async function getCupcakes() {
    const resp = await axios.get(`${BASE_URL}/api/cupcakes`);
    data = resp.data.cupcakes;
    populate(data)
}

$("#cupcake-form").on("submit", async function (evt) {
    evt.preventDefault();
    let flavor = $("#form-flavor").val();
    let rating = $("#form-rating").val();
    let size = $("#form-size").val();
    let photo_url = $("#form-photo_url").val();

    const newResp = await axios.post(`${BASE_URL}/api/cupcakes`, {
        flavor,
        rating,
        size,
        photo_url
    });

    let cupcake = newResp.data.cupcake;
    const newCup = makeCupcake(cupcake);
    $("#cupcakes-list").append(newCup);
    $("#cupcake-form").trigger("reset");
});

$(getCupcakes);