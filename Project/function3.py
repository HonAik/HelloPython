"""
定义一个函数,用于根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额。

具体规则如下:

· 优惠券需要商品金额满5000才可以使用,且优惠券金额不能超过商品总价。

· 积分抵扣需要商品总金额满5000才可以使用,100积分抵扣1元(且抵扣金额不能超过商品总价,积分只能整百抵扣)。

"""

#user input

#function for calculation
def cal(*order : tuple[str,float,int],coupon =0, score=0,delivery):
    #total price = price*amount-coupon - scores + delivery

    #p * a
    total_price = [i[1]*i[2] for i in order]
    total_cost = sum(total_price)

    #coupon
    if total_cost >=5000 and coupon <= total_cost:
        total_cost -= coupon
    
    #scores
    if total_cost >=5000 and score // 100 <= total_cost:
        
        if score // 100 !=0:
            print("Cannot use scores that undivisible by 100")

        else:
            scoretoprice = score%100
            total_cost -= scoretoprice
    
    #delivery fee
    total_cost += delivery
    
    return total_cost

#call
total = cal(("Computer",1000,1),("book",12,4),("apple",10,5),coupon=40,score=200,delivery=10)
print(f"the total is {total}")