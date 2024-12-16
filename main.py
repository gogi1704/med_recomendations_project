# import recomendation_model
# import zhaloba_validation_model
import zhaloba_final_result_model
import puzzle_bot_api


# async def get_recs(user_id, topic , user_info ):
#     answer = await recomendation_model.get_recomendations(topic , user_info)
#     change_result = await puzzle_bot_api.change_var_puzzle(user_id, answer)

#     if  change_result['code']== 0:
#         send_command_result = await puzzle_bot_api.send_command_neuro_recs(user_id)

#         if send_command_result['code']!= 0 :
#             await puzzle_bot_api.send_command_error(user_id)
#     else : 
#         await puzzle_bot_api.send_command_error(user_id)


async def get_recs(user_id, user_anketa , user_zhaloba ):
    answer = await zhaloba_final_result_model.get_zhaloba_result(user_anketa , user_zhaloba)
    change_result = await puzzle_bot_api.change_var_puzzle(user_id, answer)

    if  change_result['code']== 0:
        send_command_result = await puzzle_bot_api.send_command_neuro_recs(user_id)

        if send_command_result['code']!= 0 :
            await puzzle_bot_api.send_command_error(user_id)
    else : 
        await puzzle_bot_api.send_command_error(user_id)

# async def get_zhaloba_result(user_id, user_anketa, zhaloba ):
#     answer = await zhaloba_final_result_model.get_zhaloba_result(user_anketa , zhaloba)

