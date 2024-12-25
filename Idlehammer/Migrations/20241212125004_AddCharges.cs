using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace CSharpClicker.Web.Migrations
{
    /// <inheritdoc />
    public partial class AddCharges : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<int>(
                name: "CurrentCharge",
                table: "UserBoosts",
                type: "INTEGER",
                nullable: false,
                defaultValue: 0);

            migrationBuilder.AddColumn<int>(
                name: "MaxCharge",
                table: "Boosts",
                type: "INTEGER",
                nullable: false,
                defaultValue: 0);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "CurrentCharge",
                table: "UserBoosts");

            migrationBuilder.DropColumn(
                name: "MaxCharge",
                table: "Boosts");
        }
    }
}
