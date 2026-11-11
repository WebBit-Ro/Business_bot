import asyncio
import logging

from aiogram import Bot, Dispatcher, F, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import BOT_TOKEN, MANAGER_USERNAME
from content import CONTENT

router = Router()


def build_main_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    buttons = CONTENT["buttons"]

    builder.button(
        text=buttons["services"],
        callback_data="page:services",
    )
    builder.button(
        text=buttons["faq"],
        callback_data="page:faq",
    )
    builder.button(
        text=buttons["hours_location"],
        callback_data="page:hours_location",
    )
    builder.button(
        text=buttons["contact"],
        callback_data="page:contact",
    )
    builder.adjust(2, 2)

    return builder.as_markup()


def build_back_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=CONTENT["buttons"]["back"],
        callback_data="page:home",
    )

    return builder.as_markup()


def build_contact_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=CONTENT["buttons"]["message_manager"],
        url=f"https://t.me/{MANAGER_USERNAME}",
    )
    builder.button(
        text=CONTENT["buttons"]["back"],
        callback_data="page:home",
    )
    builder.adjust(1)

    return builder.as_markup()


@router.message(CommandStart())
async def handle_start(message: Message) -> None:
    welcome_text = CONTENT["welcome"].format(
        business_name=CONTENT["business_name"]
    )
    await message.answer(
        text=welcome_text,
        reply_markup=build_main_menu(),
    )


@router.callback_query(F.data.startswith("page:"))
async def handle_menu_navigation(callback: CallbackQuery) -> None:
    if not isinstance(callback.message, Message):
        await callback.answer()
        return

    page = (callback.data or "").removeprefix("page:")

    if page == "home":
        text = CONTENT["welcome"].format(
            business_name=CONTENT["business_name"]
        )
        keyboard = build_main_menu()
    elif page in {"services", "faq", "hours_location", "contact"}:
        text = CONTENT[page]
        keyboard = (
            build_contact_menu()
            if page == "contact"
            else build_back_menu()
        )
    else:
        await callback.answer(
            text="This menu option is unavailable.",
            show_alert=True,
        )
        return

    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=keyboard,
        )
    except TelegramBadRequest as error:
        if "message is not modified" not in str(error).casefold():
            logging.warning("Menu update failed: %s", error)
            await callback.answer(
                text="Couldn't update the menu. Please try again.",
                show_alert=True,
            )
            return

    await callback.answer()


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dispatcher = Dispatcher()
    dispatcher.include_router(router)

    try:
        await dispatcher.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
