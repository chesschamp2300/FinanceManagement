var principle = document.getElementById("principle");
var interest = document.getElementById("iRate");
var mPayment = document.getElementById("mMpayment");
var period = document.getElementById('termType')


principle.addEventListener("input", )

// principle.addEventListener("keyup", function(event) {
// if (event.keyCode === 13) {
//     event.preventDefault();
//     document.getElementById("mybutton").click();
// }
// });
interest.addEventListener("keyup", function(event) {
if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("mybutton").click();
}
});
mPayment.addEventListener("keyup", function(event) {
if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("mybutton").click();
}
});


function calculateInterest(principle,iRate,period,payment)
{
    var runningPrinciple = [principle];
    var runningInterest = [0.0];
    var totalInterest = 0.0;
    var rValue = (iRate/period);
    var nextValue = 0;

    while((principle - payment) > 0){
        if((principle - payment) > 0){   //check to ensure repayment doesnt go negative
            //calculate next running value
            nextValue = ((1+rValue)*principle  ) - payment;
            runningPrinciple.push(nextValue);
        }
        else{
            //set running principle to 0 to show loan is paid off
            runningPrinciple.push(0);
        }
        //calculate interest for this cycle
        runningInterest.push((rValue*principle));
        //calculate total interest 
        totalInterest += runningInterest[runningInterest.length-1];
        principle = runningPrinciple[runningPrinciple.length-1];
    }
    //return and array containing runningPrinciple, runningInterest, totalInterest 
    return [runningPrinciple, runningInterest, totalInterest];
}