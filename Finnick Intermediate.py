# %%
from instagramy import InstagramUser as IU

givenUN = input("Enter a valid and existing Intagram username: ") 
unInstance = IU(givenUN)
followersNumber1 = unInstance.number_of_followers
postsNumber1 =  unInstance.number_of_posts
print (givenUN + " has " + str(followersNumber1) + " followers and " + str(postsNumber1) + " posts")

givenUN2 = input("Enter a valid and existing Intagram username: ") 
unInstance2 = IU(givenUN2)
followersNumber2 = unInstance2.number_of_followers
postsNumber2 =  unInstance2.number_of_posts
print (givenUN2 + " has " + str(followersNumber2) + " followers and " + str(postsNumber2) + " posts")

givenUN3 = input("Enter a valid and existing Intagram username: ") 
unInstance3 = IU(givenUN3)
followersNumber3 = unInstance3.number_of_followers
postsNumber3 =  unInstance3.number_of_posts
print (givenUN3 + " has " + str(followersNumber3) + " followers and " + str(postsNumber3) + " posts")

ratio1 = followersNumber1/postsNumber1
ratio2 = followersNumber2/postsNumber2
ratio3 = followersNumber3/postsNumber3

print (givenUN + " has a ratio of " + str(ratio1))
print (givenUN2 + " has a ratio of " + str(ratio2))
print (givenUN3 + " has a ratio of " + str(ratio3))
most_successful =  max(ratio1, ratio2, ratio3)
print ("The most successful Instagram account has a ratio of " + str(most_successful))





# %%
