$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('#date_joined').datetimepicker({
        format: 'YYYY-DD-MM',
        date: moment().format("YYYY-DD-MM"),
        locale: 'es',
        //maxDate: moment().format("YYYY-DD-MM")
    });

    $("input[name='iva']").TouchSpin({
        min: 0,
        max: 100,
        step: 0.1,
        decimals: 2,
        boostat: 5,
        maxboostedstep: 10,
        postfix: '%',
        buttondown_class: 'btn btn-secondary',
        buttonup_class: 'btn btn-secondary',
    })
});

$(function () {

});
