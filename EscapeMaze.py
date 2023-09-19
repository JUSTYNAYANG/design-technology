t = (f" /////////    //   //      ///////                ///////      //      //     // //\n"
     f"    //        //   //      //                     //           // //   //     //   //\n"
     f"    //        ///////      ///////                ///////      //  //  //     //    //\n"
     f"    //        //   //      //                     //           //   // //     //   //\n"
     f"    //        //   //      ///////                ///////      //      //     // //\n")

d = (f" //     //    //////     //     //                // //        ///////      ///////     // //\n"
     f"  //  //     //   //     //     //                //   //        //         //          //   //\n"
     f"    //       //   //     //     //                //    //       //         //////      //    //\n"
     f"    //       //   //      //    //                //   //        //         //          //   //\n"
     f"    //       //////        /////                  // //        ///////      ///////     // //\n")

while True:
    print("\n")
    print(
        f"//////     //////        ///          //          ////////     ///////                  //           //        //          ////////    ///////\n"
        f"//         ///         //   //       // //        //     //    //                       // //     // //       // //            //      //\n"
        f"////         ///       //           ///////       ///////      ///////                  //  //   //  //      ///////         //        ///////\n"
        f"//             ///     //   //     //     //      //           //                       //   // //   //     //     //      //          //\n"
        f"//////     //////       ///       //       //     //           ///////                  //    //     //    //       //    ////////     ///////\n")

    walk = 0
    print(
        "You wake up alone, in a cold, dim maze, all is quiet. The smooth wall seems to be around 5 meters tall, impossible to scale. With no food and water, you know that right now all you need is to survive.  Remember though, a mistake could cost your life.")

    a = input("\nPlease type 'begin' to start the game.  ")
    if a.lower() == "begin":
        print(
            "You wander aimlessly through the maze, unsure of what to do next. It has been ten minutes since you regained concious. You wonder whether or not to stay at the starting point, to wait for someone to save you or move on and explore the maze?")
        a = input("\nStay or Move? ")
        if a.lower() == "stay":
            print(
                "You choose to stay, hoping someone would save you. However, it passed 2 days, no one came, you are now starving and thirsty. What will you do?")
            a = input("\nStay or Leave? ")
            if a.lower() == "stay":
                print(
                    "Fortunately someone came as soon as you decided to stay.  They fed you some water and fruits.  You feel so much better! The person beckons you to follow them.  Do you want to trust the person and follow them home?")
                a = input("\nYes or No? ")
                if a.lower() == "yes":
                    print(
                        "You followed them finding yourself in the middle of a parade.   For some unknown reason, your body starts to dance along.  You aren't able to stop.")
                    a = input("\nDance? ")
                    if a.lower() == "dance":
                        print(
                            "Few years later...You are still in the parade. Food comes by once a while.  The people are also really nice.  But like everyone else you just can't stop dancing.  Who was the person that brought you here? No one knows. This is your dancing life.\n")
                        print(t)
                        break
                    else:
                        print("That is not an option.\n")
                        print(d)
                        break
                else:
                    print(
                        "You wander around. Yet this time, you don't meet anyone or find anything. Due to dehydration.your death comes near.\n")
                    print(d)
                    break
            else:
                print(
                    "Oh no!  Your situation was much worst than you expected.  Suddenly moving took a toll on your body.  You couldn't stand the pain and collasped.\n")
                print(d)
                break
        else:
            print("You keep moving on, you meet a corner, and it’s time to decide to turn left or right.")
            a = input("\nLeft or Right? ")
            if a.lower() == "left":
                print(
                    "Left: You decided to turn left, the moment you do so, you see a lion that is being released from the cage. You become friend with the lion, and he brings you through a shortcut. When you arrive the next corner, he leaves after dipping his head at you in farewell.")
                a = input("\nRight? ")
                if a.lower() == "right":
                    print(
                        "Right: You turn right, and you see a village in this maze, there are humans, dog, cow, chicken, and farmland. People in this village  find and cultivate enough resources to be self-sufficient. Do you want to stay at this village or move on?")
                    a = input("\nStay or Move? ")
                    if a.lower() == "stay":
                        print(
                            "Stay: You choose to stay at this village, giving up your life you had before you found yourself in the maze. You  spend the rest of your long and fulfilling life in this beautiful village. \n")
                        print(t)
                        break
                    else:
                        print("Move on: You walk back to where you came from")
                        a = input("\nWalk? ")
                        if a.lower() == "walk":
                            walk = 1
                        else:
                            print("That is not an option.\n")
                            print(d)
                            break
                else:
                    print("That is not an option. \n")
                    print(d)
                    break
            else:
                print(
                    "Right: As you keep walking, you see a light, and there is a door at the end. You open it, next second, you notice that it is right in front of your house. You walk in and see the maze again, you are shocked because it disappeared. You became desperate to go back home, but you still continued your journey to the maze.")
                a = input("\nWalk? ")
                if a.lower() == "walk":
                    walk = 1
                else:
                    print("That is not an option.\n")
                    print(d)
                    break

    if walk == 1:
        print("You walked more further into the maze and saw a big tree. Do you want to walk towards the tree?")
        a = input("\nYes or No? ")
        if a.lower() == "Yes":
            print(
                "The tree has a hole which is a big portal that could bring you back home when you go through it. You step into the portal. You succesfully arrive back home. \n")
            print(t)
            break
        else:
            print(
                "The tree is a spirit tree.  Since you ignored it, it was offended that you didn't appreciate the beauty of it. To punish you, the tree formed its roots into a prison and placed you inside. \n")
            print(t)
            break

